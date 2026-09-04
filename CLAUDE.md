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

A healthy run currently reports ~21,600 questions and 94/94 topics; those
numbers grow as banks are added, so treat the paragraph above as a shape, not a
constant. 0 failures is the part that matters.

Three extra suites cover what `test-flows.mjs` does not:

    node check_ui24.mjs    # All / Not done yet mode, resource links
    node check_sync.mjs    # merge correctness + offline degradation
    node check_pave.mjs    # sign-in banner states + the PAVE virtual category

`check_pave.mjs` exists because `VIRTUAL_CATS` resolves ids through
`FLOW_BY_ID` and then calls `.filter(Boolean)` — a typo'd id does not throw, it
silently removes the topic from the category. It also asserts that shared
topics are the SAME object as in their home category (so one set of progress
stats follows a topic) and that the guest banner really says "guest".

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
- Categories can be added as *virtual* categories via `VIRTUAL_CATS`, which maps
  sub-section names to existing flow ids. Nothing is copied, so the WIFA
  checklist stays a single source of truth and one set of progress stats follows
  a topic no matter which category it was opened from.
