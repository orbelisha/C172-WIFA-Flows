import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await b.newPage();
const pageErrors = [];
p.on('pageerror', e => pageErrors.push(String(e)));
await p.goto('file:///home/claude/C172-WIFA-Flows/index.html');
await p.waitForFunction(() => window.__ppl);

const out = await p.evaluate(() => {
  const P = window.__ppl, m = P.Sync._merge, r = {};

  // 1. phone answered later than laptop -> phone wins
  const local  = { items: { 'PFRegs::0': { r:1, w:0, at: 100 } }, topics: {}, settings: {} };
  const remote = { items: { 'PFRegs::0': { r:0, w:1, at: 200 } }, topics: {}, settings: {} };
  r.laterWins = m(local, remote).items['PFRegs::0'].w === 1;

  // 2. and the reverse direction
  const local2  = { items: { 'PFRegs::0': { r:1, w:0, at: 300 } }, topics: {}, settings: {} };
  r.laterWinsReverse = m(local2, remote).items['PFRegs::0'].r === 1;

  // 3. an item only one side has is never lost
  const a = { items: { 'A::1': { r:1,w:0,at:5 } }, topics: {}, settings: {} };
  const bb= { items: { 'B::2': { r:0,w:1,at:6 } }, topics: {}, settings: {} };
  const mm = m(a, bb).items;
  r.noItemLost = !!mm['A::1'] && !!mm['B::2'];

  // 4. topics: best is the max of both, runs never inflates
  const lt = { items:{}, settings:{}, topics: { T: { runs:3, best:80, last:80, lastAt: 100, correct:5, wrong:1 } } };
  const rt = { items:{}, settings:{}, topics: { T: { runs:2, best:95, last:60, lastAt: 200, correct:4, wrong:3 } } };
  const t = m(lt, rt).topics.T;
  r.bestIsMax = t.best === 95;
  r.runsNotSummed = t.runs === 3;
  r.laterDrillWins = t.last === 60;

  // 5. merging twice must be stable (idempotent) - no counter drift
  const once = m(lt, rt), twice = m(once, rt);
  r.idempotent = JSON.stringify(once.topics.T) === JSON.stringify(twice.topics.T);

  // 6. empty cloud doc must not wipe local progress
  const wiped = m(lt, { items:{}, topics:{}, settings:{} });
  r.emptyRemoteSafe = wiped.topics.T.runs === 3;

  // 7. offline: SDK blocked in this sandbox, so sync must report unavailable
  r.notReadyOffline = P.Sync.isReady() === false;
  r.notSignedIn = P.Sync.isSignedIn() === false;

  // 8. the app must still work with sync dead
  const flow = P.ALL_FLOWS.find(f => f.id === 'PFRegs');
  r.drillStillWorks = P.buildTopicDrill(flow, 10).length === 10;
  P.Store.save();                       // wrapped save must not throw
  r.saveSurvives = true;
  return r;
});
out.pageErrors = pageErrors;
console.log(JSON.stringify(out, null, 2));
await b.close();
