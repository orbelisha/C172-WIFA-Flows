/**
 * Automated test harness for C172-WIFA-Flows index.html
 *
 * Runs the real app in headless Chromium and drives it through window.__ppl.
 * index.html itself stays dependency-free; this harness is a dev tool only and
 * is never loaded by the app.
 *
 * Requires playwright:  npm install --no-save playwright
 *
 * Usage: node test-flows.mjs [path-to-index.html] [questions-per-flow]
 *        defaults to the index.html sitting next to this script.
 * Exit code 0 = every check passed. Non-zero = do not push.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const FILE = path.resolve(process.argv[2] || path.join(HERE, 'index.html'));
const PER_FLOW = Number(process.argv[3] || 400);

if (!fs.existsSync(FILE)) {
  console.error(`FATAL: ${FILE} not found`);
  process.exit(2);
}

const run = async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const consoleErrors = [];
  const pageErrors = [];
  const netWarnings = [];
  page.on('console', m => { if (m.type() !== 'error') return; const t = m.text();
    if (/Failed to load resource|net::ERR_/.test(t)) netWarnings.push(t); else consoleErrors.push(t); });
  page.on('pageerror', e => pageErrors.push(String(e && e.message || e)));

  await page.goto('file://' + FILE, { waitUntil: 'load' });
  await page.waitForFunction(() => !!window.__ppl, null, { timeout: 15000 });

  /* ============================================================
     PART A — generator soundness over thousands of questions
     ============================================================ */
  const partA = await page.evaluate((perFlow) => {
    const P = window.__ppl;
    const { ALL_FLOWS, generateOne, norm, splitItem, stripTags, validOptions } = P;

    const failures = [];
    const stats = { generated: 0, nulls: 0, byKind: {}, byFlow: {} };
    const fail = (flow, kind, msg, q) => {
      if (failures.length < 200) {
        failures.push({
          flow: flow.id, title: flow.title, kind,
          msg,
          question: q ? stripTags(q.question).replace(/\s+/g, ' ').trim().slice(0, 180) : null,
          options: q ? q.options : null,
          answer: q ? q.options[q.correct] : null
        });
      }
    };

    const keyOf = (item) => { const p = splitItem(item); return norm(p ? p.key : item); };
    // The app renders prompts through esc(); compare against the escaped form.
    const escHtml = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    const unesc = s => String(s).replace(/&quot;/g, '"').replace(/&gt;/g, '>').replace(/&lt;/g, '<').replace(/&amp;/g, '&');

    ALL_FLOWS.forEach(flow => {
      if (flow.type === 'mcq' || flow.type === 'info') return;

      const items = flow.items;
      const normItems = items.map(norm);
      const itemSet = new Set(normItems);
      const keySet = new Set(items.map(keyOf));
      const firstIndexOf = (s) => normItems.indexOf(norm(s));

      // key -> set of values it legitimately stands for
      const keyVals = {};
      items.forEach(it => {
        const p = splitItem(it);
        if (!p) return;
        (keyVals[norm(p.key)] = keyVals[norm(p.key)] || new Set()).add(norm(p.val));
      });

      stats.byFlow[flow.id] = { generated: 0, nulls: 0 };

      for (let n = 0; n < perFlow; n++) {
        const q = generateOne(flow);
        if (!q) { stats.nulls++; stats.byFlow[flow.id].nulls++; continue; }
        stats.generated++;
        stats.byFlow[flow.id].generated++;
        stats.byKind[q.kind] = (stats.byKind[q.kind] || 0) + 1;

        const opts = q.options;
        const ans = opts[q.correct];
        const distractors = opts.filter((_, i) => i !== q.correct);
        const qText = stripTags(q.question);

        /* ---- universal invariants ---- */
        if (!validOptions(opts)) fail(flow, q.kind, 'validOptions() rejected the option set', q);
        if (new Set(opts.map(norm)).size !== opts.length) fail(flow, q.kind, 'DUPLICATE ANSWER: two options are the same text', q);
        if (q.correct < 0 || q.correct >= opts.length) fail(flow, q.kind, 'correct index out of range', q);
        if (opts.some(o => !String(o).trim())) fail(flow, q.kind, 'empty option', q);
        if (opts.length < 3) fail(flow, q.kind, 'fewer than 3 options', q);
        if (q.sourceId !== flow.id) fail(flow, q.kind, 'sourceId does not match the flow', q);

        /* ---- per-kind soundness ---- */
        switch (q.kind) {
          case 'next': {
            const ai = q.anchor;
            if (typeof ai !== 'number' || ai < 1 || ai >= items.length) { fail(flow, q.kind, 'anchor out of range', q); break; }
            if (norm(ans) !== normItems[ai]) fail(flow, q.kind, 'answer is not items[anchor]', q);
            if (qText.indexOf(escHtml(items[ai - 1])) === -1) fail(flow, q.kind, 'prompt item is not the one preceding the answer', q);
            if (normItems.filter(x => x === normItems[ai - 1]).length !== 1) fail(flow, q.kind, 'prompt item is not unique in the flow — question has two valid answers', q);
            distractors.forEach(d => { if (norm(d) === normItems[ai]) fail(flow, q.kind, 'distractor equals the answer', q); });
            break;
          }
          case 'prev': {
            const ai = q.anchor;
            if (typeof ai !== 'number' || ai < 0 || ai >= items.length - 1) { fail(flow, q.kind, 'anchor out of range', q); break; }
            if (norm(ans) !== normItems[ai]) fail(flow, q.kind, 'answer is not items[anchor]', q);
            if (qText.indexOf(escHtml(items[ai + 1])) === -1) fail(flow, q.kind, 'prompt item is not the one following the answer', q);
            if (normItems.filter(x => x === normItems[ai + 1]).length !== 1) fail(flow, q.kind, 'prompt item is not unique in the flow — question has two valid answers', q);
            if (!distractors.every(d => itemSet.has(norm(d)))) fail(flow, q.kind, 'distractor is not from this flow', q);
            break;
          }
          case 'order': {
            if (!opts.every(o => itemSet.has(norm(o)))) { fail(flow, q.kind, 'an option is not from this flow', q); break; }
            const idxs = opts.map(firstIndexOf);
            if (q.correct !== 0) fail(flow, q.kind, 'correct is not index 0 before shuffling', q);
            for (let k = 1; k < idxs.length; k++) {
              if (!(idxs[k - 1] < idxs[k])) fail(flow, q.kind, `options are not in true flow order (${idxs.join(',')})`, q);
            }
            opts.forEach(o => { if (normItems.filter(x => x === norm(o)).length !== 1) fail(flow, q.kind, 'an option appears twice in the flow — "which comes first" is ambiguous', q); });
            break;
          }
          case 'first': {
            if (norm(ans) !== normItems[0]) fail(flow, q.kind, 'answer is not the first item of the flow', q);
            if (!distractors.every(d => itemSet.has(norm(d)))) fail(flow, q.kind, 'distractor is not from this flow', q);
            break;
          }
          case 'last': {
            if (norm(ans) !== normItems[normItems.length - 1]) fail(flow, q.kind, 'answer is not the last item of the flow', q);
            if (!distractors.every(d => itemSet.has(norm(d)))) fail(flow, q.kind, 'distractor is not from this flow', q);
            break;
          }
          case 'notin': {
            // The ANSWER must be foreign; the DISTRACTORS must belong to the flow.
            if (itemSet.has(norm(ans))) fail(flow, q.kind, 'FOREIGN-ITEM BUG: the "NOT part of" answer IS part of this flow', q);
            if (keySet.has(keyOf(ans))) fail(flow, q.kind, 'FOREIGN-ITEM BUG: the answer\'s key already exists in this flow (same item, different wording)', q);
            distractors.forEach(d => { if (!itemSet.has(norm(d))) fail(flow, q.kind, 'a distractor is NOT in the flow — the question has two correct answers', q); });
            break;
          }
          case 'deffwd': {
            const m = /(?:what does|items )\s*(.*?)\s*(?:stand for|stands for)/i.exec(qText);
            const key = m ? norm(unesc(m[1])) : null;
            if (key && keyVals[key]) {
              if (!keyVals[key].has(norm(ans))) fail(flow, q.kind, 'answer is not a value this key stands for', q);
              distractors.forEach(d => {
                if (keyVals[key].has(norm(d))) fail(flow, q.kind, 'AMBIGUOUS: a distractor is also a valid meaning of the same key', q);
              });
            }
            break;
          }
          case 'defrev': {
            const ansKey = norm(ans);
            if (!keyVals[ansKey]) fail(flow, q.kind, 'answer is not a key in this flow', q);
            distractors.forEach(d => { if (norm(d) === ansKey) fail(flow, q.kind, 'distractor equals the answer key', q); });
            // the quoted value must map to exactly this key
            const m = /which one means\s*[“"”']?(.+?)[”"']?\s*\??$/i.exec(qText.trim());
            if (m) {
              const val = norm(unesc(m[1]));
              const owners = Object.keys(keyVals).filter(k => keyVals[k].has(val));
              if (owners.length > 1) fail(flow, q.kind, 'AMBIGUOUS: that meaning belongs to more than one key', q);
              if (owners.length === 1 && owners[0] !== ansKey) fail(flow, q.kind, 'answer key does not own the quoted meaning', q);
              distractors.forEach(d => { if (keyVals[norm(d)] && keyVals[norm(d)].has(val)) fail(flow, q.kind, 'a distractor key also means the quoted value', q); });
            }
            break;
          }
          default:
            fail(flow, q.kind, 'unknown question kind', q);
        }
      }
    });

    return { failures, stats };
  }, PER_FLOW);

  /* ============================================================
     PART B — drill integrity (no repeats inside one drill)
     ============================================================ */
  const partB = await page.evaluate(() => {
    const P = window.__ppl;
    const { ALL_FLOWS, buildTopicDrill, buildMixedDrill, norm, stripTags } = P;
    const problems = [];
    const short = [];

    ALL_FLOWS.forEach(flow => {
      if (flow.type === 'info') return;
      for (let rep = 0; rep < 5; rep++) {
        const want = 20;
        const drill = buildTopicDrill(flow, want);
        const seen = new Set();
        drill.forEach(q => {
          const sig = q.kind + '|' + norm(stripTags(q.question)) + '|' + norm(q.options[q.correctAnswer]);
          if (seen.has(sig)) problems.push({ flow: flow.id, msg: 'duplicate question inside one topic drill', sig: sig.slice(0, 140) });
          seen.add(sig);
          if (new Set(q.options.map(norm)).size !== q.options.length) problems.push({ flow: flow.id, msg: 'duplicate answer text inside a drill question', sig: sig.slice(0, 140) });
          if (q.correctAnswer < 0 || q.correctAnswer >= q.options.length) problems.push({ flow: flow.id, msg: 'correctAnswer index out of range after finalize()' });
        });
        if (drill.length === 0) problems.push({ flow: flow.id, msg: 'topic drill produced ZERO questions' });
        else if (drill.length < want && rep === 0) short.push({ flow: flow.id, title: flow.title, got: drill.length, want, type: flow.type, items: flow.items.length });
      }
    });

    const scopes = ['all'].concat(Object.keys(P.appDatabase));
    scopes.forEach(scope => {
      for (let rep = 0; rep < 3; rep++) {
        const drill = buildMixedDrill(scope, 30);
        const seen = new Set();
        drill.forEach(q => {
          const sig = q.kind + '|' + norm(stripTags(q.question)) + '|' + norm(q.options[q.correctAnswer]);
          if (seen.has(sig)) problems.push({ flow: 'MIXED:' + scope, msg: 'duplicate question inside one mixed drill', sig: sig.slice(0, 140) });
          seen.add(sig);
        });
        if (drill.length === 0) problems.push({ flow: 'MIXED:' + scope, msg: 'mixed drill produced ZERO questions' });
      }
    });

    return { problems, short };
  });

  /* ============================================================
     PART C — navigation smoke test through the real UI
     ============================================================ */
  let partC = { problems: ['PART C DID NOT RUN'], opened: 0, topicLinkCount: 0, drills: 0 };
  try {
    partC = await page.evaluate(async () => {
      const problems = [];
      const sleep = ms => new Promise(r => setTimeout(r, ms));
      const $ = id => document.getElementById(id);
      const activePage = () => {
        const a = Array.from(document.querySelectorAll('.page.active')).map(e => e.id);
        return a.length === 1 ? a[0] : ('AMBIGUOUS:' + JSON.stringify(a));
      };
      const expect = (want, ctx) => { const got = activePage(); if (got !== want) problems.push(`${ctx}: expected ${want}, got ${got}`); };

      // --- 1. sidebar: every category, then every topic under it ---
      // Since Version 5 the sidebar interleaves group headings (.sidebar-group)
      // with the category entries, so filter to the ones that are categories.
      const catDivs = Array.from(document.querySelectorAll('#sidebarCats > div'))
        .filter(d => d.querySelector('.sidebar-item .sidebar-text'));
      if (!catDivs.length) problems.push('left menu built no category entries');
      let opened = 0, topicLinkCount = 0;

      for (const div of catDivs) {
        const catBtn = div.querySelector('.sidebar-item .sidebar-text');
        const iconBtn = div.querySelector('.sidebar-item .sidebar-icon');
        const catName = catBtn.textContent;
        catBtn.click(); await sleep(15);
        expect('categoryScreen', `category "${catName}"`);

        iconBtn.click(); await sleep(15);
        const topicBtns = Array.from(div.querySelectorAll('.sidebar-sub button'));
        topicLinkCount += topicBtns.length;
        for (const tb of topicBtns) {
          const title = tb.textContent;
          tb.click(); await sleep(10);
          opened++;
          expect('studyScreen', `topic "${title}"`);
          if ($('studyTitle').textContent !== title) problems.push(`topic "${title}": studyScreen shows "${$('studyTitle').textContent}"`);
          iconBtn.click(); await sleep(5); // menu is closed by showPage; re-expand
        }
      }

      // --- 2. main nav buttons ---
      const navMap = { home: 'homeScreen', mixed: 'mixedScreen', progress: 'progressScreen' };
      for (const key of Object.keys(navMap)) {
        const b = document.querySelector(`#leftNavMenuContent [data-nav="${key}"]`);
        if (!b) { problems.push(`no [data-nav="${key}"] button`); continue; }
        b.click(); await sleep(15);
        expect(navMap[key], `nav "${key}"`);
      }

      // --- 3. run a full drill end-to-end on a few topics of each type ---
      const P = window.__ppl;
      const sample = [];
      ['sequence', 'definition', 'mcq'].forEach(t => {
        P.ALL_FLOWS.filter(f => f.type === t).slice(0, 3).forEach(f => sample.push(f));
      });
      let drills = 0;
      for (const flow of sample) {
        const div = catDivs.find(d => (d.querySelector('.sidebar-item .sidebar-text') || {}).textContent === flow.parentCat);
        if (!div) { problems.push(`no sidebar entry for category ${flow.parentCat}`); continue; }
        div.querySelector('.sidebar-icon').click(); await sleep(10);
        const tb = Array.from(div.querySelectorAll('.sidebar-sub button')).find(b => b.textContent === flow.title);
        if (!tb) { problems.push(`no sidebar entry for topic ${flow.title}`); continue; }
        tb.click(); await sleep(10);

        $('mainStartBtn').click(); await sleep(20);
        if (activePage() !== 'quizScreen') { problems.push(`drill "${flow.title}": start did not open quizScreen (got ${activePage()})`); continue; }

        let guard = 0;
        while (activePage() === 'quizScreen' && guard++ < 120) {
          const opts = Array.from(document.querySelectorAll('#optionsContainer .option-btn'));
          if (!opts.length) { problems.push(`drill "${flow.title}": question rendered with no options`); break; }
          if (opts.length < 2) problems.push(`drill "${flow.title}": question rendered with ${opts.length} option`);
          opts[0].click(); await sleep(8);
          const nb = $('nextBtn');
          if (nb.style.display === 'none') { problems.push(`drill "${flow.title}": Continue button stayed hidden after answering`); break; }
          nb.click(); await sleep(10);
        }
        if (guard >= 120) problems.push(`drill "${flow.title}": did not terminate within 120 questions`);
        if (activePage() !== 'scoreScreen') problems.push(`drill "${flow.title}": ended on ${activePage()}, expected scoreScreen`);
        else drills++;

        // --- 4. back button must walk up to home and then hide itself ---
        let hops = 0;
        while (activePage() !== 'homeScreen' && hops++ < 10) { $('backBtn').click(); await sleep(20); }
        if (activePage() !== 'homeScreen') problems.push(`back button never reached home from "${flow.title}" (stuck on ${activePage()})`);
        if ($('backBtn').style.display !== 'none') problems.push('back button still visible on home screen');
      }

      return { problems, opened, topicLinkCount, drills };
    });
  } catch (e) {
    partC = { problems: ['PART C CRASHED: ' + e.message], opened: 0, topicLinkCount: 0, drills: 0 };
  }

  await browser.close();

  /* ============================================================
     REPORT
     ============================================================ */
  const A = partA.failures.length;
  const B = partB.problems.length;
  const C = partC.problems.length;
  const errs = consoleErrors.length + pageErrors.length;

  console.log('='.repeat(72));
  console.log('C172-WIFA-Flows automated test run');
  console.log('file: ' + FILE);
  console.log('='.repeat(72));
  console.log(`A. questions generated : ${partA.stats.generated}  (null returns: ${partA.stats.nulls})`);
  console.log('   by kind             : ' + JSON.stringify(partA.stats.byKind));
  console.log(`A. soundness failures  : ${A}`);
  console.log(`B. drill problems      : ${B}`);
  console.log(`C. navigation problems : ${C}  (topics opened: ${partC.opened}/${partC.topicLinkCount}, full drills: ${partC.drills})`);
  console.log(`   console/page errors : ${errs}`);
  console.log('');

  if (partB.short.length) {
    console.log('--- NOTE: topics that could not fill a 20-question drill (not a failure, but a ceiling) ---');
    partB.short.forEach(s => console.log(`    ${s.flow} (${s.title}) type=${s.type} items=${s.items} -> ${s.got}/${s.want}`));
    console.log('');
  }

  const dump = (title, list) => {
    if (!list.length) return;
    console.log(`--- ${title} ---`);
    const grouped = {};
    list.forEach(f => {
      const k = (f.flow || '?') + ' | ' + (f.kind || '') + ' | ' + f.msg;
      (grouped[k] = grouped[k] || []).push(f);
    });
    Object.keys(grouped).slice(0, 40).forEach(k => {
      const g = grouped[k];
      console.log(`  [${g.length}x] ${k}`);
      const e = g[0];
      if (e.question) console.log(`        Q: ${e.question}`);
      if (e.options) console.log(`        options: ${JSON.stringify(e.options)}`);
      if (e.answer) console.log(`        answer:  ${e.answer}`);
      if (e.sig) console.log(`        sig: ${e.sig}`);
    });
    console.log('');
  };

  dump('A. GENERATOR SOUNDNESS FAILURES', partA.failures);
  dump('B. DRILL PROBLEMS', partB.problems);
  if (C) { console.log('--- C. NAVIGATION PROBLEMS ---'); partC.problems.slice(0, 20).forEach(p => console.log('  ' + p)); console.log(''); }
  if (pageErrors.length) { console.log('--- UNCAUGHT PAGE ERRORS ---'); pageErrors.slice(0, 20).forEach(e => console.log('  ' + e)); console.log(''); }
  if (netWarnings.length) { console.log('--- NETWORK WARNINGS (external resource, not a push blocker) ---'); Array.from(new Set(netWarnings)).slice(0,10).forEach(e => console.log('  ' + e)); console.log(''); }
  if (consoleErrors.length) { console.log('--- CONSOLE ERRORS ---'); consoleErrors.slice(0, 20).forEach(e => console.log('  ' + e)); console.log(''); }

  const total = A + B + C + errs;
  console.log('='.repeat(72));
  console.log(total === 0 ? 'RESULT: PASS — safe to push' : `RESULT: FAIL — ${total} problem(s). DO NOT PUSH.`);
  console.log('='.repeat(72));
  process.exit(total === 0 ? 0 : 1);
};

run().catch(e => { console.error('HARNESS CRASHED:', e); process.exit(3); });
