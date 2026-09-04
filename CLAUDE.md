# C172-WIFA-Flows

Single self-contained app: `index.html`. No build step.

As of v3.0.0 it loads the Firebase compat SDK from the gstatic CDN for
optional cross-device progress sync. That is the ONLY dependency, it is
loaded by `<script src>` with no bundler, and everything behind it is
guarded: if the CDN is unreachable or the user never signs in, the app runs
exactly as before on localStorage alone. Keep it that way — sync must never
become load-bearing.
Served live from `main` via GitHub Pages at
https://orbelisha.github.io/C172-WIFA-Flows/

## Working agreement

Or is the only user of this repo. Push finished work **straight to `main`** —
do not open a PR, do not park it on a side branch, do not ask for confirmation
first. Just make sure it passed the tests below.

## Before every push

Run `test-flows.mjs` against the edited `index.html`. It drives the real app in
headless Chromium through `window.__ppl` and checks question-generator
soundness, drill integrity, and UI navigation.

    npm install --no-save playwright   # once per machine
    node test-flows.mjs                # defaults to ./index.html

Exit code 0 = safe to push. Anything else = do not push.

A healthy run reports 18,000 questions generated with 0 soundness failures,
0 drill problems, 66/66 topics opened, 8 full drills, and 0 console errors.

The harness is a dev tool only — `index.html` never loads it and stays
dependency-free.

A `net::ERR_CONNECTION_RESET` or `ERR_TUNNEL_CONNECTION_FAILED` network
warning is an external resource (Google Fonts, and since v3.0.0 the Firebase
SDK) and is not a push blocker; the harness classifies it as such itself.
Those warnings appearing in a sandbox run is also the offline-degradation
path being exercised — the run must still report 0 drill and 0 navigation
problems, which is the proof that sync stayed optional.

A healthy run currently reports ~24,100 questions and 71/71 topics
(71 = every topic exactly once, which is itself the one-parent check); those
numbers grow as banks are added, so treat the paragraph above as a shape, not a
constant. 0 soundness failures is the part that matters.

`null returns` in part A is NOT a failure and does not need chasing. It counts
the times the generator declined to build a question from a random draw — most
often because the only available distractors were too close to the answer to be
fair. It went from 0 to ~280 in Version 6 purely because the new FAR banks have
many items sharing a leading token ("Part 1 ➜", "Part 43 ➜", "91.3 ➜",
"91.103 ➜"), so more draws get refused. The check that matters is the
"could not fill a 20-question drill" list: only banks whose item COUNT is below
20 should appear there. A definition topic with 20+ items showing up in that
list is a real problem.

Three extra suites cover what `test-flows.mjs` does not:

    node check_ui24.mjs    # All / Not done yet mode, resource links
    node check_sync.mjs    # merge correctness + offline degradation
    node check_pave.mjs    # one-parent-only, grouped home, topic picker, banner,
                           # and that FAR Navigation stays a top-level category

`check_pave.mjs` guards the structural invariants that fail SILENTLY rather
than throwing: a topic appearing under two parents, `parentCat` disagreeing with
where the topic actually sits, a category unreachable from the home screen, and
the Mixed Drill topic picker not actually filtering the drill it builds. It also
checks the top-bar home button and the guest sign-in banner.

`check_sync.mjs` is the important one before touching sync: it asserts that
the later answer wins in both directions, that no item from either side is
lost, that `best` is a max and `runs` never inflates, that merging twice is
idempotent, and that an EMPTY cloud document cannot wipe local progress.

## Conventions

- Line endings are LF, enforced by `.gitattributes` (`*.html text eol=lf`).
  Never reintroduce CRLF — it makes the diff look like the whole file changed.
- The footer version is a plain integer plus the date it shipped:
  `<div class="footer">Version N &middot; DD.MM.YYYY | ...`. Bump N by 1 for each
  user-visible change and set the date to that day. No semver, no dot-releases —
  Or wants to read the footer and know at a glance which build he is on and
  whether it is current. Version 3 = 04.09.2026 is the baseline.
- **A topic belongs to exactly ONE parent category.** Or asked for this
  explicitly in Version 5: virtual categories used to show the same topic under
  several parents, and that is what made the home screen unreadable. Every topic
  now has one home in `appDatabase`. `VIRTUAL_CATS` still exists as a mechanism
  but is deliberately empty — filling it puts a topic under two parents again.
  `check_pave.mjs` fails the build if that happens.
- The home screen and side menu group categories via `CAT_GROUPS`
  (In the Cockpit / Look It Up / Ground Knowledge / Exam Prep). A category
  missing from that list still renders, under "More", so adding one can never
  make it vanish — but put it in a group.
