// Structure and shell checks (Version 5).
//
// The big invariant here is Or's rule that a topic belongs to exactly ONE
// parent category. Before Version 5 the app used VIRTUAL_CATS to show the same
// topic under several parents, which is what made the home screen unreadable.
// Nothing in the app throws if that regresses — a topic simply starts showing
// up twice — so it is asserted here.
//
// Also covers: the PAVE category's contents, the grouped home screen, the
// Mixed Drill topic picker, the top-bar home button and the sign-in banner.
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';

const file = process.argv[2] || './index.html';
const browser = await chromium.launch();
const page = await browser.newPage();
const pageErrors = [];
page.on('pageerror', e => pageErrors.push(String(e)));
await page.goto(pathToFileURL(file).href);
await page.waitForFunction(() => !!window.__ppl, null, { timeout: 15000 });

const EXPECTED_PAVE = {
    'The Framework': ['PAVE'],
    'P — Pilot': ['IMSAFE'],
    'A — Aircraft': ['ARROW', 'AV1ATE', 'ATOMATO', 'FLAPS'],
    'V — enVironment': ['NWKRAFT', 'NOTAMTypes'],
    'E — External Pressures': ['ExternalP'],
    'FAA Trick Questions': ['PAVETraps']
};
const EXPECTED_GROUPS = ['In the Cockpit', 'Look It Up', 'Ground Knowledge', 'Exam Prep'];

const out = await page.evaluate((expected) => {
    const r = {};
    const P = window.__ppl;
    const CATS = P.CATS, byId = P.FLOW_BY_ID;

    // --- ONE PARENT PER TOPIC ---------------------------------------
    const homes = {};
    Object.keys(CATS).forEach(cat => {
        Object.keys(CATS[cat]).forEach(sub => {
            CATS[cat][sub].forEach(f => {
                (homes[f.id] = homes[f.id] || []).push(cat + '/' + sub);
            });
        });
    });
    r.multiParent = Object.keys(homes).filter(id => {
        const cats = new Set(homes[id].map(h => h.split('/')[0]));
        return cats.size > 1;
    }).map(id => id + ' -> ' + homes[id].join(' , '));
    r.duplicatedInSameCat = Object.keys(homes).filter(id => homes[id].length > 1
        && new Set(homes[id].map(h => h.split('/')[0])).size === 1);
    r.topicCount = Object.keys(homes).length;
    r.allFlowsMatchesTree = P.ALL_FLOWS.length === r.topicCount;
    r.virtualCatsEmpty = Object.keys(P.VIRTUAL_CATS || {}).length === 0;
    // parentCat must agree with where the topic actually sits
    r.parentCatWrong = Object.keys(homes).filter(id =>
        byId[id] && byId[id].parentCat !== homes[id][0].split('/')[0]);

    // --- PAVE contents ----------------------------------------------
    const pave = CATS['Oral Exam — PAVE'];
    r.paveExists = !!pave;
    r.paveMissing = [];
    if (pave) {
        Object.keys(expected.pave).forEach(sub => {
            const got = (pave[sub] || []).map(f => f.id);
            expected.pave[sub].forEach(id => {
                if (got.indexOf(id) === -1) r.paveMissing.push(sub + '/' + id);
            });
        });
    }
    // SAFETY is a passenger briefing, not a PAVE pillar item — it belongs to Acronyms
    r.safetyInAcronyms = !!byId['SAFETY'] && byId['SAFETY'].parentCat === 'Acronyms';
    // the emergency material has one home now
    r.emergenciesOwnsAbcd = !!byId['ABCD'] && byId['ABCD'].parentCat === 'Emergencies';
    r.emergenciesOwnsFire = !!byId['ElecFire'] && byId['ElecFire'].parentCat === 'Emergencies';
    // FAR navigation is its own top-level category, a peer of POH Navigation,
    // NOT a sub-section of PAVE.
    r.farIsTopLevel = !!CATS['FAR Navigation'];
    // FARParts was dropped in Version 7 — it duplicated FARPeripheral
    r.farPartsGone = !byId['FARParts'];
    r.farNoteRendered = (function () {
        P.renderCategory && P.renderCategory('FAR Navigation', 'replace');
        const d = document.querySelector('#catContent details.cat-note');
        return { exists: !!d, rows: d ? d.querySelectorAll('dt').length : 0,
                 collapsed: d ? d.open === false : null,
                 first: d ? (d.querySelector('dt') || {}).textContent : null };
    })();
    // POH: the ordering bank must not give the numbers away, and a separate
    // bank must map number to title in both directions.
    const po = byId['POHOrder'], pn = byId['POHNumbers'];
    r.pohOrderHasNoNumbers = !!po && po.items.every(i => !/^\s*\d/.test(i));
    r.pohOrderCount = po ? po.items.length : 0;
    r.pohOrderFirst = po ? po.items[0] : null;
    r.pohNumbersExists = !!pn && pn.type === 'definition';
    r.pohNumbersCount = pn ? pn.items.length : 0;
    r.pohNumbersMapsBoth = !!pn && pn.items.every(i => /^Section \d ➔ .+/.test(i));
    r.farSubs = CATS['FAR Navigation'] ? Object.keys(CATS['FAR Navigation']) : [];
    r.farTopics = CATS['FAR Navigation']
        ? Object.values(CATS['FAR Navigation']).flat().map(f => f.id) : [];
    r.farTriad = (CATS['FAR Navigation'] && CATS['FAR Navigation']['The Core Triad'] || []).map(f => f.id);
    const findIt = byId['FARFindIt'];
    r.farFindItCount = findIt ? findIt.items.length : 0;
    r.farFindItValid = !!findIt && findIt.items.every(it =>
        it.question && Array.isArray(it.options) && it.options.length >= 2 &&
        typeof it.correctAnswer === 'number' &&
        it.correctAnswer >= 0 && it.correctAnswer < it.options.length &&
        it.explanation && it.explanation.length > 40);

    // --- Stage 1 (Version 10) ----------------------------------------
    const s1 = CATS['Stage 1'];
    r.stage1Exists = !!s1;
    r.stage1Banks = s1 ? Object.values(s1).flat().map(f => f.id + ':' + f.items.length) : [];
    r.stage1Total = s1 ? Object.values(s1).flat().reduce((n, f) => n + f.items.length, 0) : 0;
    r.stage1AllValid = !!s1 && Object.values(s1).flat().every(f =>
        f.type === 'mcq' && Array.isArray(f.resources) && f.resources.length > 0 &&
        f.items.every(it =>
            it.question && Array.isArray(it.options) && it.options.length >= 3 &&
            new Set(it.options).size === it.options.length &&
            typeof it.correctAnswer === 'number' &&
            it.correctAnswer >= 0 && it.correctAnswer < it.options.length &&
            it.explanation && it.explanation.length > 60));
    // the bank's `text` must match its real item count
    r.stage1CountsMatch = !!s1 && Object.values(s1).flat().every(f =>
        f.text === f.items.length + ' questions');

    // --- per-category exam block (Version 11) -------------------------
    r.catDrill = (function () {
        P.setCatPickedIds('Stage 1', null);
        P.renderCategory('Stage 1', 'replace');
        const box = document.querySelector('#catContent .cat-drill');
        if (!box) return { exists: false };
        const chips = () => Array.from(box.querySelectorAll('[data-cat-topic]'));
        const btn = () => box.querySelector('#catStartBtn');
        const res = { exists: true, chips: chips().length,
                      allSelected: chips().every(c => c.classList.contains('selected')),
                      fullLabel: btn().textContent };
        // deselect one subject -> label changes and the drill narrows
        chips()[0].click();
        res.afterDeselectLabel = btn().textContent;
        res.stored = (P.catPickedIds('Stage 1') || []).length;
        const narrowed = P.catDrillFlows('Stage 1');
        res.narrowedCount = narrowed.length;
        res.narrowedExcludesFirst = !narrowed.some(f => f.id === 'S1Aero');
        // and it must NOT have touched the Mixed Drill's own selection
        res.mixedUntouched = P.Store.data.settings.mixedTopics === undefined;
        // the drill it builds must only use the picked subjects
        const q = P.buildDrillFromFlows(narrowed, 30);
        res.drillOnlyPicked = q.length > 0 && q.every(x =>
            narrowed.some(f => f.id === x.sourceId));
        // None disables Start, All restores it
        box.querySelector('#catPickNone').click();
        res.noneDisables = btn().disabled === true;
        box.querySelector('#catPickAll').click();
        res.allRestores = chips().every(c => c.classList.contains('selected'))
            && btn().disabled === false && P.catPickedIds('Stage 1') === null;
        res.restoredLabel = btn().textContent;
        // a single-topic category gets no block
        P.renderCategory('Weather', 'replace');
        res.onWeather = !!document.querySelector('#catContent .cat-drill');
        return res;
    })();

    const traps = byId['PAVETraps'];
    r.trapsCount = traps ? traps.items.length : 0;
    r.trapsAllValid = !!traps && traps.items.every(it =>
        it.question && Array.isArray(it.options) && it.options.length >= 2 &&
        typeof it.correctAnswer === 'number' &&
        it.correctAnswer >= 0 && it.correctAnswer < it.options.length &&
        it.explanation && it.explanation.length > 40);
    r.noDoubleEscape = !!traps && traps.resources.every(x => x.label.indexOf('&amp;') === -1);

    // --- grouped home screen -----------------------------------------
    P.renderHome && P.renderHome('replace');
    const labels = Array.from(document.querySelectorAll('#homeCategories .section-label')).map(e => e.textContent);
    r.homeGroups = labels;
    r.homeCards = Array.from(document.querySelectorAll('#homeCategories .parent-card'))
        .map(b => b.childNodes[0].textContent.trim());
    r.everyCatOnHome = Object.keys(CATS).every(c => r.homeCards.indexOf(c) !== -1);
    r.noCardTwice = r.homeCards.length === new Set(r.homeCards).size;

    // --- top-bar home button -----------------------------------------
    const hb = document.getElementById('homeBtn');
    r.homeBtnExists = !!hb;
    if (hb) {
        P.renderMixedScreen && P.renderMixedScreen('replace');
        const before = (document.querySelector('.page.active') || {}).id;
        hb.click();
        r.homeBtnLeftMixed = before === 'mixedScreen';
        r.homeBtnLandsHome = (document.querySelector('.page.active') || {}).id === 'homeScreen';
    }

    // --- Mixed Drill topic picker ------------------------------------
    P.renderMixedScreen('replace');
    const chips = () => Array.from(document.querySelectorAll('#topicPick .topic-chip'));
    r.pickerRendered = chips().length;
    r.pickerAllSelectedByDefault = chips().every(c => c.classList.contains('selected'));

    const first = chips()[0];
    const firstId = first.getAttribute('data-topic');
    first.click();                                   // deselect one
    r.afterDeselect = !chips()[0].classList.contains('selected');
    r.settingsRecorded = Array.isArray(P.Store.data.settings.mixedTopics)
        && P.Store.data.settings.mixedTopics.indexOf(firstId) === -1;
    // and the drill must actually stop drawing from it
    const drill = P.buildMixedDrill('all', 40);
    r.drillSkipsDeselected = drill.length > 0 && !drill.some(q => q.sourceId === firstId);

    // --- multi-select scope (Version 9) ------------------------------
    P.setMixedScopes(null);
    P.renderMixedScreen('replace');
    const scopeChips = () => Array.from(document.querySelectorAll('#scopeChips .chip'));
    r.scopeAllSelectedByDefault = (scopeChips().find(c => c.getAttribute('data-scope') === 'all') || {})
        .className.indexOf('selected') !== -1;
    const pick = name => scopeChips().find(c => c.getAttribute('data-scope') === name);
    pick('Weather').click();
    pick('Acronyms').click();
    r.twoScopesSelected = ['Weather', 'Acronyms'].every(n => pick(n).className.indexOf('selected') !== -1);
    r.allDeselectedWhenScoped = pick('all').className.indexOf('selected') === -1;
    r.scopesStored = (P.Store.data.settings.mixedScopes || []).slice().sort().join(',');
    // the picker and the drill must both honour BOTH categories
    const pickedCats = new Set(P.scopeFlows(P.mixedScopes()).map(f => f.parentCat));
    r.scopeFlowsSpansBoth = pickedCats.size === 2
        && pickedCats.has('Weather') && pickedCats.has('Acronyms');
    r.pickerHeadings = Array.from(document.querySelectorAll('#topicPick .topic-pick-cat')).map(e => e.textContent);
    const multiDrill = P.buildMixedDrill(P.mixedScopes(), 40);
    const drillCats = new Set(multiDrill.map(q => (P.FLOW_BY_ID[q.sourceId] || {}).parentCat));
    r.drillSpansBoth = drillCats.size === 2 && drillCats.has('Weather') && drillCats.has('Acronyms');
    r.drillLabel = P.scopeLabel(P.mixedScopes());
    // tapping "All Topics" clears the set again
    pick('all').click();
    r.allTopicsClears = P.mixedScopes() === null;
    // an old single-string setting must migrate rather than be ignored
    delete P.Store.data.settings.mixedScopes;
    P.Store.data.settings.mixedScope = 'Weather';
    r.legacyMigrates = (P.mixedScopes() || []).join(',') === 'Weather';
    P.setMixedScopes(null);
    P.renderMixedScreen('replace');

    document.getElementById('topicPickNone').click();
    r.noneClearsAll = chips().every(c => !c.classList.contains('selected'));
    r.startDisabledWhenEmpty = document.getElementById('mixedStartBtn').disabled === true;

    document.getElementById('topicPickAll').click();
    r.allRestores = chips().every(c => c.classList.contains('selected'));
    r.allClearsSetting = P.Store.data.settings.mixedTopics === undefined;
    r.startEnabledAgain = document.getElementById('mixedStartBtn').disabled === false;

    // --- sign-in banner (guest in a headless run) --------------------
    const box = document.getElementById('syncBanner');
    r.bannerIsGuest = !!box && box.className.indexOf('is-guest') !== -1;
    r.bannerSaysGuest = /guest/i.test((document.getElementById('syncBannerTitle') || {}).textContent || '');

    return r;
}, { pave: EXPECTED_PAVE });

out.pageErrors = pageErrors;

const fail = [];
const req = (cond, msg) => { if (!cond) fail.push(msg); };

req(out.multiParent.length === 0, 'topics under more than one parent: ' + out.multiParent.join(' | '));
req(out.duplicatedInSameCat.length === 0, 'topic listed twice in one category: ' + out.duplicatedInSameCat.join(', '));
req(out.parentCatWrong.length === 0, 'parentCat disagrees with the tree: ' + out.parentCatWrong.join(', '));
req(out.allFlowsMatchesTree, 'ALL_FLOWS does not match the category tree');
req(out.virtualCatsEmpty, 'VIRTUAL_CATS is non-empty — that reintroduces multi-parent topics');
req(out.paveExists, 'Oral Exam — PAVE category missing');
req(out.paveMissing.length === 0, 'PAVE is missing: ' + out.paveMissing.join(', '));
req(out.safetyInAcronyms, 'SAFETY should live in Acronyms, not PAVE');
req(out.emergenciesOwnsAbcd, 'ABCD should live in Emergencies');
req(out.emergenciesOwnsFire, 'ElecFire should live in Emergencies');
req(out.farIsTopLevel, 'FAR Navigation must be its own top-level category');
req(out.farPartsGone, 'FARParts should have been dropped — it duplicated FARPeripheral');
['FAR61', 'FAR91', 'FAR141School', 'FAR141', 'FARPeripheral', 'FAR43', 'NTSB830', 'FARCitation', 'FARFindIt']
    .forEach(id => req(out.farTopics.indexOf(id) !== -1, 'FAR Navigation is missing ' + id));
// the 61-vs-141 comparison must come LAST in the Triad, after the standalone 141
req(out.farTriad.indexOf('FAR141') === out.farTriad.length - 1,
    'FAR141 (61 vs 141) must be last in The Core Triad, got: ' + out.farTriad.join(', '));
req(out.farTriad.indexOf('FAR141School') === out.farTriad.length - 2,
    'FAR141School must sit just before the comparison, got: ' + out.farTriad.join(', '));
req(out.farNoteRendered.exists, 'the collapsed Parts index is missing from the FAR Navigation page');
req(out.farNoteRendered.collapsed === true, 'the Parts index should start collapsed');
req(out.farNoteRendered.rows >= 15, 'the Parts index is too short: ' + out.farNoteRendered.rows);
req(out.pohOrderHasNoNumbers, 'POHOrder still shows section numbers — the drill can be answered by counting');
req(out.pohOrderCount === 9, 'POHOrder should still have 9 items, got ' + out.pohOrderCount);
req(out.pohNumbersExists, 'POHNumbers bank missing');
req(out.pohNumbersCount === 9, 'POHNumbers should have 9 items, got ' + out.pohNumbersCount);
req(out.pohNumbersMapsBoth, 'POHNumbers items must be "Section N -> Title" so both directions drill');
req(out.farFindItCount >= 10, 'FARFindIt bank too small: ' + out.farFindItCount);
req(out.farFindItValid, 'a FARFindIt item is malformed');
req(out.catDrill.exists, 'the per-category exam block is missing from the Stage 1 page');
req(out.catDrill.chips === 6, 'category exam should offer 6 subject chips, got ' + out.catDrill.chips);
req(out.catDrill.allSelected, 'category exam subjects should all start selected');
req(/full exam/i.test(out.catDrill.fullLabel),
    'with everything picked the button should offer a full exam, got: ' + out.catDrill.fullLabel);
req(!/full exam/i.test(out.catDrill.afterDeselectLabel),
    'the button still says full exam after a subject was deselected');
req(out.catDrill.narrowedCount === 5, 'deselecting one subject should leave 5, got ' + out.catDrill.narrowedCount);
req(out.catDrill.narrowedExcludesFirst, 'the deselected subject is still in the drill pool');
req(out.catDrill.drillOnlyPicked, 'the category drill drew from a subject that was not picked');
req(out.catDrill.mixedUntouched, 'the category picker clobbered the Mixed Drill selection');
req(out.catDrill.noneDisables, '"None" should disable Start on the category page');
req(out.catDrill.allRestores, '"All" should reselect everything and clear the stored list');
req(/full exam/i.test(out.catDrill.restoredLabel), 'the button should offer a full exam again after All');
req(out.catDrill.onWeather === true, 'a multi-topic category should also get the exam block');
req(out.stage1Exists, 'Stage 1 category missing');
['S1Aero', 'S1Systems', 'S1Airspace', 'S1Perf', 'S1Weather', 'S1Traps'].forEach(id =>
    req(out.stage1Banks.some(b => b.indexOf(id + ':') === 0), 'Stage 1 is missing ' + id));
req(out.stage1Total >= 160, 'Stage 1 bank is too small: ' + out.stage1Total);
req(out.stage1AllValid, 'a Stage 1 item is malformed (options, answer index or explanation)');
req(out.stage1CountsMatch, 'a Stage 1 bank\'s "N questions" label disagrees with its item count');
req(out.homeCards.indexOf('Stage 1') !== -1, 'Stage 1 is not reachable from the home screen');
req(out.trapsCount >= 10, 'trick-question bank too small: ' + out.trapsCount);
req(out.trapsAllValid, 'a PAVETraps item is malformed');
req(out.noDoubleEscape, 'double-escaped entity in a resource label');
EXPECTED_GROUPS.forEach(g => req(out.homeGroups.indexOf(g) !== -1, 'home group missing: ' + g));
req(out.everyCatOnHome, 'a category is not reachable from the home screen');
req(out.noCardTwice, 'a category card appears twice on the home screen');
req(out.homeBtnExists, 'top-bar home button missing');
req(out.homeBtnLeftMixed, 'home-button test did not start from the mixed screen');
req(out.homeBtnLandsHome, 'home button did not go to the home screen');
req(out.pickerRendered > 10, 'topic picker rendered too few topics: ' + out.pickerRendered);
req(out.pickerAllSelectedByDefault, 'topics are not all selected by default');
req(out.afterDeselect, 'clicking a topic chip did not deselect it');
req(out.settingsRecorded, 'the deselection was not saved to settings');
req(out.drillSkipsDeselected, 'the mixed drill still drew from a deselected topic');
req(out.noneClearsAll, '"None" did not clear the scope');
req(out.startDisabledWhenEmpty, 'Start is not disabled with no topics picked');
req(out.allRestores, '"All" did not reselect everything');
req(out.allClearsSetting, '"All" should delete the setting, not list every id');
req(out.startEnabledAgain, 'Start stayed disabled after "All"');
req(out.scopeAllSelectedByDefault, '"All Topics" should be selected when no category is chosen');
req(out.twoScopesSelected, 'could not select two categories at once');
req(out.allDeselectedWhenScoped, '"All Topics" should clear once a category is chosen');
req(out.scopesStored === 'Acronyms,Weather', 'both scopes not stored, got: ' + out.scopesStored);
req(out.scopeFlowsSpansBoth, 'scopeFlows did not span both selected categories');
req(out.pickerHeadings.indexOf('Weather') !== -1 && out.pickerHeadings.indexOf('Acronyms') !== -1,
    'topic picker is not grouped by category, got: ' + out.pickerHeadings.join(', '));
req(out.drillSpansBoth, 'the mixed drill drew from only one of the two categories');
req(/Weather/.test(out.drillLabel) && /Acronyms/.test(out.drillLabel),
    'drill title does not name both categories: ' + out.drillLabel);
req(out.allTopicsClears, '"All Topics" did not clear the scope set');
req(out.legacyMigrates, 'an old single-string mixedScope did not migrate to mixedScopes');
req(out.bannerIsGuest && out.bannerSaysGuest, 'guest sign-in banner regressed');
req(pageErrors.length === 0, 'page errors: ' + pageErrors.join(' | '));

console.log(JSON.stringify(out, null, 2));
console.log(fail.length ? 'RESULT: FAIL\n  - ' + fail.join('\n  - ') : 'RESULT: PASS');
await browser.close();
process.exit(fail.length ? 1 : 0);
