# -*- coding: utf-8 -*-
"""Rebuild the whole "Oral Exam" category from oral_data.py + oral_data2.py,
following the ACS Area/Task structure of Or's own oral prep guide.

Replaces the existing Oral Exam block in place. Topic IDS AND ITEM ORDER are
preserved for every bank that already existed, so per-item progress
(topicId::itemIndex) survives; only the sub-section a topic sits in changes,
and that is not part of the key.
"""
import pathlib, sys
import oral_data as D1
import oral_data2 as D2
import oral_data3 as D3
import oral_data4 as D4

# ---------------------------------------------------------------- helpers
def js(s):
    out = []
    for ch in s:
        if ch == '\\':   out.append('\\\\')
        elif ch == '"':  out.append('\\"')
        elif ch == '\n': out.append('\\n')
        elif ch == '\r': continue
        elif ch in '  ': out.append('\\u%04x' % ord(ch))
        else: out.append(ch)
    return '"' + ''.join(out) + '"'

def res(pairs):
    return '[' + ', '.join('{ label: %s, url: %s }' % (js(l), js(u)) for l, u in pairs) + ']'

I8, I12 = ' ' * 16, ' ' * 12

MCQ_DESC = {
    'OralPrereq': "Everything the examiner settles before the aeroplane is even discussed: are you eligible, is the paperwork in date, and can you prove it. These are the questions that end a checkride in the first ten minutes, and they are pure bookwork — there is no excuse for losing one.",
    'OralAeromed': "The human half of the aircraft. Hypoxia, illusions, vision, medication, alcohol and fatigue — asked as scenarios rather than definitions, because what the examiner grades is what you DO about it, not that you can name it.",
    'OralInop': "The 91.213 chain, the inspection intervals and how you prove airworthiness from the logbooks. Expect the examiner to point at one broken thing and walk you all the way to a go or no-go decision.",
    'OralXC': "The planned cross-country you bring to the checkride is the spine of the oral — the examiner starts there and branches into weather, performance, airspace, fuel and diversion. Know your own plan cold.",
}
MCQ_DESC.update(D2.MCQ_DESC2)
MCQ_DESC.update(D3.MCQ_DESC3)
MCQ_DESC.update(D4.SCEN_DESC)

topics = {}

def add_def(tid, title, sub, desc, items, kind='definition'):
    body = ', '.join(js(i) for i in items)
    topics[tid] = ('{ id: %s, type: "%s", title: %s, text: %s, desc: %s, items: [%s] }'
                   % (js(tid), kind, js(title), js(sub), js(desc), body))

def add_mcq(tid, title, items, resources):
    lines = ['%s{ question: %s, options: [%s], correctAnswer: 0, explanation: %s }'
             % (I8 + '    ', js(q), ', '.join(js(o) for o in opts), js(e))
             for q, opts, e in items]
    topics[tid] = ('{\n'
        + I8 + '    id: %s,\n' % js(tid)
        + I8 + '    type: "mcq",\n'
        + I8 + '    title: %s,\n' % js(title)
        + I8 + '    text: %s,\n' % js('%d questions' % len(items))
        + I8 + '    desc: %s,\n' % js(MCQ_DESC[tid])
        + I8 + '    resources: %s,\n' % res(resources)
        + I8 + '    items: [\n' + ',\n'.join(lines) + '\n'
        + I8 + '    ]\n' + I8 + '}')

# part 1 (unchanged content, ids and item order intact)
for tid, title, sub, desc, items in D1.DEFS:
    add_def(tid, title, sub, desc, items)
# Part 4 APPENDS extra questions onto an existing bank. Appended, never
# inserted, so every existing index -- and the progress keyed to it -- holds.
def with_appends(tid, items):
    return list(items) + list(D4.APPENDS.get(tid, []))

for tid, title, items, resources in D1.BANKS:
    add_mcq(tid, title, with_appends(tid, items), resources)

# part 2 (from the guide)
for tid, title, sub, desc, items in D2.DEFS2:
    add_def(tid, title, sub, desc, items)
for tid, title, sub, desc, items in D2.SEQS2:
    add_def(tid, title, sub, desc, items, kind='sequence')
for tid, title, items, resources in D2.BANKS2:
    add_mcq(tid, title, with_appends(tid, items), resources)

# part 3 (gap-fill: the guide's unanswered headings, and questions for the
# three sub-sections that were recall-only)
for tid, title, sub, desc, items in D3.DEFS3:
    add_def(tid, title, sub, desc, items)
for tid, title, items, resources in D3.BANKS3:
    add_mcq(tid, title, with_appends(tid, items), resources)

# SPEC2 is the sub-section order; part 3 appends into existing sub-sections
# rather than adding new ones, so the ACS Task map stays intact.
bad = set(D3.INSERTS) - {t for t, _ in D2.SPEC2}
if bad:
    print('INSERTS names a sub-section that does not exist: %s' % sorted(bad), file=sys.stderr)
    sys.exit(1)
SPEC = [(t, list(ids) + D3.INSERTS.get(t, [])) for t, ids in D2.SPEC2]

# Part 4's scenario banks form their own sub-section at the end: the ACS Tasks
# are how the material is ORGANISED, scenarios are how it is ASKED.
for tid, title, items, resources in D4.SCEN_BANKS:
    add_mcq(tid, title, items, resources)
SPEC.append((D4.SCEN_SUB, [b[0] for b in D4.SCEN_BANKS]))

unused = set(D4.APPENDS) - set(topics)
if unused:
    print('APPENDS names a bank that does not exist: %s' % sorted(unused), file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------- assemble
seen = set()
secs = []
for sec_title, ids in SPEC:
    for i in ids:
        if i not in topics:
            print('UNKNOWN TOPIC ID: %s' % i, file=sys.stderr); sys.exit(1)
        if i in seen:
            print('TOPIC TWICE: %s' % i, file=sys.stderr); sys.exit(1)
        seen.add(i)
    body = ',\n'.join(I8 + topics[i] for i in ids)
    secs.append(I12 + '    %s: [\n%s\n%s    ]' % (js(sec_title), body, I12))

orphans = sorted(set(topics) - seen)
if orphans:
    print('TOPICS NOT PLACED IN ANY SUB-SECTION: %s' % orphans, file=sys.stderr); sys.exit(1)

cat = I12 + '"Oral Exam": {\n' + ',\n'.join(secs) + '\n' + I12 + '},\n'

# ---------------------------------------------------------------- splice
p = pathlib.Path('index.html')
s = p.read_text(encoding='utf-8')

start = s.find(I12 + '"Oral Exam": {')
end = s.find(I12 + '"Personal Focus": {')
if start == -1 or end == -1 or end <= start:
    print('ANCHOR FAIL: could not bracket the Oral Exam block', file=sys.stderr); sys.exit(1)
s = s[:start] + cat + s[end:]

p.write_text(s, encoding='utf-8')
print('Oral Exam rebuilt: %d sub-sections, %d topics, %d questions'
      % (len(secs), len(topics),
         sum(len(b[2]) for b in D1.BANKS) + sum(len(b[2]) for b in D2.BANKS2)
         + sum(len(b[2]) for b in D3.BANKS3) + sum(len(b[2]) for b in D4.SCEN_BANKS)
         + sum(len(v) for v in D4.APPENDS.values())),
      file=sys.stderr)
