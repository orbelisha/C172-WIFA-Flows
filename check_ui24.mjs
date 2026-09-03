import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await b.newPage();
const errs = [];
p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
p.on('pageerror', e => errs.push(String(e)));
await p.goto('file:///home/claude/C172-WIFA-Flows/index.html');
await p.waitForFunction(() => window.__ppl);

const out = await p.evaluate(async () => {
  const P = window.__ppl, $ = id => document.getElementById(id);
  const flow = P.ALL_FLOWS.find(f => f.id === 'PFRegs');
  const r = {};

  // fresh profile: everything unseen
  P.renderStudyScreen(flow, 'replace', 'Personal Focus');
  r.modeChips = [...$('modeChips').querySelectorAll('button')].map(b => b.textContent);
  r.resourceLinks = [...$('studyResources').querySelectorAll('a')].map(a => ({t: a.textContent, u: a.href}));
  r.hintAll = $('drillHint').textContent;

  // mark all but the last 2 items as already answered (bank size changes as items are appended)
  const N = flow.items.length;
  const seenUpTo = N - 2;
  for (let i = 0; i < seenUpTo; i++) P.Store.data.items['PFRegs::' + i] = { r: 1, w: 0, at: Date.now() };
  P.Store.save();

  // switch to "not done yet"
  P.Store.data.settings.unseenOnly = true;
  P.renderStudyScreen(flow, 'replace', 'Personal Focus');
  r.modeChipsAfter = [...$('modeChips').querySelectorAll('button')].map(b => b.textContent);
  r.hintUnseen = $('drillHint').textContent;
  r.lengthChips = [...$('lengthChips').querySelectorAll('button')].map(b => b.textContent);

  // the drill must contain ONLY the two unanswered items (indices 20,21)
  const drill = P.buildTopicDrill(flow, 15);
  const qs = drill.map(q => q.question);
  const expect = [seenUpTo, seenUpTo + 1].map(i => flow.items[i].question);
  r.bankSize = N;
  r.drillLen = drill.length;
  r.onlyUnseen = qs.every(x => expect.some(e => x.indexOf(e.slice(0, 40)) !== -1));

  // exhausted case: mark all seen, unseenOnly should fall back to whole bank
  for (let i = 0; i < flow.items.length; i++) P.Store.data.items['PFRegs::' + i] = { r: 1, w: 0, at: Date.now() };
  P.renderStudyScreen(flow, 'replace', 'Personal Focus');
  r.hintExhausted = $('drillHint').textContent;
  r.fallbackLen = P.buildTopicDrill(flow, 15).length;
  r.unseenChipDisabled = [...$('modeChips').querySelectorAll('button')][1].disabled;

  // a non-mcq flow must hide the mode chips and the resources block
  P.renderStudyScreen(P.ALL_FLOWS.find(f => f.type === 'sequence'), 'replace');
  r.seqModeHidden = $('modeChips').style.display === 'none';
  r.seqResHidden = $('studyResources').style.display === 'none';
  return r;
});
out.consoleErrors = errs;
console.log(JSON.stringify(out, null, 2));
await b.close();
