# -*- coding: utf-8 -*-
"""Oral Exam, part 5 — the last six gaps from the printed guide.

A term-by-term sweep of the ASA guide against the app found six headings with
no coverage at all. They are answered here as questions APPENDED to the
existing bank for their Area — appended, never inserted, so every existing
index (and the progress keyed to topicId::itemIndex) is untouched and these
six arrive as unanswered.

Two of them are places where the guide, printed in 2017, is now simply wrong:
HIWAS was decommissioned on 8 January 2020, and the MEL/91.213 split is the
part of airworthiness people most often learn backwards. Both are written to
the CURRENT rule, not to the book.

PPL scope throughout: no IMC, no partial panel, no approaches.
"""

APPENDS5 = {

 # --- I.B Airworthiness ---------------------------------------------
 'OralInop': [
  ("What is a Minimum Equipment List, and does your trainer have one?",
   ["An FAA-approved list, issued to a specific aircraft by serial number under a Letter of Authorization, permitting flight with named items inoperative — and most trainers do not have one.",
    "The list of instruments and equipment in 91.205 that every aircraft must carry.",
    "The equipment list in the POH showing what was installed at the factory."],
   "A MEL is not a list of what you must have — it is permission to fly WITHOUT certain things. It is aircraft-specific, approved by the FSDO, and the MEL plus its LOA become airworthiness documents that must be carried. The trap: if your aircraft HAS a MEL you must use it, and 91.213(d) is closed to you. Most training aeroplanes have none, which is exactly why 91.213(d) is the path you actually fly."),
  ("No MEL, and the landing light fails before a day VFR flight. Walk the examiner through 91.213(d).",
   ["Confirm it is not required by the type certificate, the KOEL, 91.205 or an AD; then remove or deactivate it, placard it INOPERATIVE, and make the airworthiness determination.",
    "Placard it inoperative and go — a landing light is never required for day VFR.",
    "The aircraft is unairworthy until a mechanic repairs or removes the item."],
   "The examiner wants the CHAIN, not the verdict. Four gates first — type certificate, Kinds of Operation Equipment List, 91.205, any AD — then remove or deactivate, then the placard, then the determination. A pilot may do the deactivation and placarding only where no maintenance is involved; otherwise it is a mechanic's job. Reaching the right answer by the wrong route still loses the question."),
  ("What are the two kinds of Airworthiness Directive, and what makes one an emergency AD?",
   ["Those requiring immediate compliance before further flight, and those requiring compliance within a specified period — an emergency AD skips the usual notice and comment because the unsafe condition will not wait.",
    "Mandatory ADs and advisory ADs, the second of which an owner may decline.",
    "Airframe ADs and engine ADs, issued by the manufacturer."],
   "ADs live in 14 CFR Part 39 and compliance is mandatory under 91.403 — there is no such thing as an optional AD. Emergency ADs are issued without the normal rulemaking comment period and are sent directly to the registered owners of the affected aircraft. Watch for RECURRING ADs: complied with once is not complied with, and the logbook must show the interval being met."),
  ("The aircraft has a GPS installed after it left the factory. What must be on board because of it?",
   ["The AFM Supplement for that equipment — it is part of the FAA-approved flight manual and carries the limitations and procedures for it.",
    "Nothing extra; the original AFM covers all installed equipment.",
    "Only the manufacturer's user guide, which is advisory."],
   "Optional or STC'd equipment arrives with a supplement, and that supplement is FAA-approved AFM material — so 91.9, which requires you to operate within the AFM, reaches it. The W in ARROW is the weight and balance data, and a supplement that changes the equipment list changes that too. An examiner who sees an avionics stack with no matching supplements has found a real discrepancy."),
 ],

 # --- I.C Weather ----------------------------------------------------
 'OralWxQ': [
  ("The briefer mentions a trough across your route. What is it, and why do you care?",
   ["An elongated area of relatively LOW pressure — air converges and rises along it, so expect cloud, showers and a wind shift as you cross.",
    "An elongated area of relatively HIGH pressure, bringing settled air and good visibility.",
    "The boundary between two air masses of the same temperature."],
   "Trough low, ridge high — and the consequence follows from the pressure, not the name. Low means convergence and rising air, which builds cloud and precipitation; high means subsidence, which suppresses it but traps haze and smoke underneath. Crossing a trough gives you a wind shift, which is the practical reason the examiner asks on a cross-country."),
  ("Your 2017 study guide tells you to tune a VOR for HIWAS. What should you say?",
   ["That HIWAS no longer exists — it was decommissioned on 8 January 2020, and in-flight hazard information now comes from FIS-B, Flight Service, or ATC.",
    "That HIWAS is still broadcast, but only on VORs marked with a circled H.",
    "That HIWAS was replaced by TWEB in the contiguous United States."],
   "The FAA ended Hazardous Inflight Weather Advisory Service broadcasts on 8 January 2020, citing collapsed demand. What replaced it: FIS-B over ADS-B In, Flight Service on the radio, and controllers, who advise of hazardous weather within 150 NM of their sector. TWEB was an Alaska service and was never the replacement. This is worth knowing precisely — a lot of printed material still teaches the old answer."),
 ],

 # --- I.F Performance ------------------------------------------------
 'OralPerfQ': [
  ("Distinguish angle of incidence from angle of attack.",
   ["Incidence is the FIXED angle built between the wing chord line and the longitudinal axis; angle of attack is the angle between the chord line and the relative wind, and it changes constantly in flight.",
    "They are two names for the same angle, measured from different reference points.",
    "Incidence is the angle to the relative wind; angle of attack is the angle to the horizon."],
   "Incidence is a rigging decision made in the factory — you cannot change it from the cockpit. Angle of attack is what you control, what the wing actually responds to, and what stalls the aeroplane. The reason the examiner pairs them is the follow-up: because the stall happens at a fixed critical ANGLE OF ATTACK, the wing can stall at any airspeed and any attitude."),
 ],
}
