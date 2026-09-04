// Version 4 checks: the top-of-home sign-in banner, and the PAVE oral-exam
// category. The virtual-category builder silently drops ids it cannot resolve
// (`.filter(Boolean)`), so a typo would just make a sub-section vanish rather
// than throw — these assertions are what catch that.
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';

const file = process.argv[2] || './index.html';
const browser = await chromium.launch();
const page = await browser.newPage();
const pageErrors = [];
page.on('pageerror', e => pageErrors.push(String(e)));
await page.goto(pathToFileURL(file).href);
await page.waitForFunction(() => !!window.__ppl, null, { timeout: 15000 });

const EXPECTED = {
    'The Framework': ['PAVE', 'FARParts'],
    'P — Pilot': ['IMSAFE', 'SAFETY'],
    'A — Aircraft': ['ARROW', 'AV1ATE', 'ATOMATO', 'FLAPS'],
    'V — enVironment': ['NWKRAFT', 'NOTAMTypes'],
    'E — External Pressures': ['ExternalP'],
    'FAA Trick Questions': ['PAVETraps']
};

const out = await page.evaluate((expected) => {
    const r = {};

    // --- banner, guest state (nobody is signed in in a headless run) ---
    const box = document.getElementById('syncBanner');
    r.bannerExists = !!box;
    r.bannerIsGuest = !!box && box.className.indexOf('is-guest') !== -1;
    r.bannerSaysGuest = /guest/i.test((document.getElementById('syncBannerTitle') || {}).textContent || '');
    r.bannerBtnExists = !!document.getElementById('syncBannerBtn');
    // it must sit above the page title, not below it
    const h1 = document.querySelector('#homeScreen h1');
    r.bannerAboveTitle = !!box && !!h1 &&
        (box.compareDocumentPosition(h1) & Node.DOCUMENT_POSITION_FOLLOWING) !== 0;
    r.bannerVisibleOnHome = !!box && box.getBoundingClientRect().height > 0;

    // --- PAVE category resolves completely ---
    const cats = window.__ppl.CATS || {};
    const pave = cats['Oral Exam — PAVE'];
    r.categoryExists = !!pave;
    r.missing = [];
    r.subsections = {};
    if (pave) {
        Object.keys(expected).forEach(sub => {
            const got = (pave[sub] || []).map(f => f.id);
            r.subsections[sub] = got;
            expected[sub].forEach(id => { if (got.indexOf(id) === -1) r.missing.push(sub + '/' + id); });
        });
    }

    // --- shared topics are the SAME objects, not copies, so progress follows ---
    const byId = window.__ppl.FLOW_BY_ID || {};
    r.arrowIsShared = !!pave && (pave['A — Aircraft'] || []).some(f => f === byId['ARROW']);

    // --- the trick-question bank is well formed ---
    const traps = byId['PAVETraps'];
    r.trapsCount = traps ? traps.items.length : 0;
    r.trapsAllValid = !!traps && traps.items.every(it =>
        it.question && Array.isArray(it.options) && it.options.length >= 2 &&
        typeof it.correctAnswer === 'number' &&
        it.correctAnswer >= 0 && it.correctAnswer < it.options.length &&
        it.explanation && it.explanation.length > 40);
    r.trapsHasResources = !!traps && Array.isArray(traps.resources) && traps.resources.length > 0;
    // labels must not carry double-escaped entities (regression from v2.5.0)
    r.noDoubleEscape = !!traps && traps.resources.every(x => x.label.indexOf('&amp;') === -1);

    // --- no duplicate ids anywhere ---
    const ids = Object.keys(byId);
    r.uniqueIds = ids.length === new Set(ids).size;

    return r;
}, EXPECTED);

out.pageErrors = pageErrors;

const fail = [];
if (!out.bannerExists) fail.push('sign-in banner missing');
if (!out.bannerIsGuest) fail.push('banner not in guest state when signed out');
if (!out.bannerSaysGuest) fail.push('banner does not say "guest"');
if (!out.bannerBtnExists) fail.push('banner sign-in button missing');
if (!out.bannerAboveTitle) fail.push('banner is not above the page title');
if (!out.bannerVisibleOnHome) fail.push('banner not visible on the home screen');
if (!out.categoryExists) fail.push('Oral Exam — PAVE category missing');
if (out.missing.length) fail.push('unresolved ids: ' + out.missing.join(', '));
if (!out.arrowIsShared) fail.push('ARROW was copied instead of shared — progress would fork');
if (out.trapsCount < 10) fail.push('trick-question bank too small: ' + out.trapsCount);
if (!out.trapsAllValid) fail.push('a PAVETraps item is malformed');
if (!out.trapsHasResources) fail.push('PAVETraps has no video resources');
if (!out.noDoubleEscape) fail.push('double-escaped entity in a resource label');
if (!out.uniqueIds) fail.push('duplicate topic id');
if (pageErrors.length) fail.push('page errors: ' + pageErrors.join(' | '));

console.log(JSON.stringify(out, null, 2));
console.log(fail.length ? 'RESULT: FAIL\n  - ' + fail.join('\n  - ') : 'RESULT: PASS');
await browser.close();
process.exit(fail.length ? 1 : 0);
