# C172-WIFA-Flows

Single self-contained app: `index.html`. No build step, no dependencies.
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

A `net::ERR_CONNECTION_RESET` network warning is an external resource and is
not a push blocker; the harness classifies it as such itself.

## Conventions

- Line endings are LF, enforced by `.gitattributes` (`*.html text eol=lf`).
  Never reintroduce CRLF — it makes the diff look like the whole file changed.
- Bump the version in the footer (`<div class="footer">vX.Y.Z | ...`) with each
  user-visible change.
- Categories can be added as *virtual* categories via `VIRTUAL_CATS`, which maps
  sub-section names to existing flow ids. Nothing is copied, so the WIFA
  checklist stays a single source of truth and one set of progress stats follows
  a topic no matter which category it was opened from.
