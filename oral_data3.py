# -*- coding: utf-8 -*-
"""Oral Exam, part 3 — closing the gaps found by comparing the app against
Or's prep guide ("PPL Oral Exam Preparation Questions", Liraz Bershadsky).

Two kinds of gap, both taken from the guide itself rather than from anywhere
else:

1. THREE SUB-SECTIONS HAD NO QUESTIONS AT ALL — The Checkride, I.C Weather and
   I.F Performance were recall banks only. A definition bank teaches the list;
   it does not test whether he can apply it, which is what the examiner does.

2. HEADINGS IN THE GUIDE WITH NO ANSWER WRITTEN UNDER THEM. Liraz listed the
   question and left the answer blank, so there was nothing to study from:
     - "VFR triangle?"  and  "Define the terms: LIFR, IFR, MVFR and VFR"
     - "How to determine your personal minimum?"
     - "What effect does a forward / aft center of gravity have?"
     - "What performance characteristics will be adversely affected when an
        aircraft has been overloaded?"
     - "What are the four turning tendencies?"
     - "How does icing affect aircraft performance?"
   Those are answered here. Section IV of the guide (Take off, landing and go
   around — "Abeam the numbers", "Final check") is also empty, but it is WIFA
   pattern procedure and inventing numbers for it would be worse than leaving
   it out. That one needs Liraz or Tomer.
"""

A = '➔'

def d(term, meaning):
    return '%s %s %s' % (term, A, meaning)

# ===================================================================
# I.C — WEATHER HAZARDS  (the guide's Task C answers)
# ===================================================================

WXHAZ = ("OralWxHazards", "Weather Hazards", "Icing, Storms, Shear & Fog",
         "Every answer here is from the Task C section of your guide. Note how many of them are a LIST with a number attached — two conditions for ice, three ingredients for a thunderstorm, three places for shear, four fogs. Examiners count.",
        [
 d('Icing needs two things', 'visible moisture, AND the aircraft surface temperature at or below 0 Celsius. Both, and the temperature that counts is at the COLLECTING SURFACE, not on the OAT gauge'),
 d('Clear ice', 'large drops freezing SLOWLY and spreading back as a smooth, heavy sheet. The heaviest and the hardest to shed'),
 d('Rime ice', 'small drops freezing on contact, fast. Opaque, rough and milky — it spoils the airflow more than it weighs'),
 d('Mixed ice', 'clear and rime forming at the same time'),
 d('Instrument ice', 'ice over the pitot tube and static port. The instruments go before the airframe feels anything, which is why pitot heat is part of the response'),
 d('How icing hurts you', 'it destroys lift by spoiling the airflow, adds weight, adds drag, and can jam a control surface. It RAISES your stall speed while CUTTING your available power — both sides of the margin at once'),
 d('If you meet icing', 'leave the visible moisture. Descend below the bases, climb above the tops, or turn back the way you came — and get the pitot heat on'),
 d('Frost', 'hazardous, and not because of its weight. The ROUGHNESS spoils the smooth airflow and causes early separation. A small amount can stop you getting airborne at all'),
 d('Thunderstorm, three ingredients', 'sufficient water vapour, an unstable lapse rate, and an initial lifting force — a front, terrain, or heating from below'),
 d('Cumulus stage', 'updraft only, and growth may exceed 3,000 fpm'),
 d('Mature stage', 'begins when precipitation reaches the ground. Updrafts over 6,000 fpm, downdrafts over 2,500. ALL thunderstorm hazards are at their greatest here'),
 d('Dissipating stage', 'downdraft throughout, and the cell dies rapidly'),
 d('Microburst', 'less than 2.5 miles across, downdrafts to 6,000 fpm, peak winds lasting under 5 minutes — though a sequence can run over 30. Convective activity only, and the mature stage only'),
 d('What a microburst does to you', 'an increasing HEADSHIFT first — performance improves and you are tempted to reduce power — then the downdraft, then the tailwind. The trap is the good part at the start'),
 d('Wind shear, three places', 'with a low-level temperature INVERSION, in a frontal zone or thunderstorm, and as clear air turbulence at altitude near a jet stream'),
 d('Temperature inversion', 'smooth stable air close to the ground, with fog, stratus or haze trapped underneath — and turbulence and wind shear at the BOUNDARY. Clear cool nights, and along frontal boundaries'),
 d('Radiation fog', 'calm wind, clear night, and the ground cooling by radiation until the air reaches its dew point. The classic dawn fog'),
 d('Advection fog', 'warm moist air moving over a cold surface. WIND IS REQUIRED for it — that is the discriminator against radiation fog. Coastal'),
 d('Upslope fog', 'moist stable air forced up a slope and cooled adiabatically to its dew point'),
 d('Steam fog', 'cold dry air over warm water. It comes with low-level turbulence AND icing, which makes it the most dangerous of the four to fly through'),
 d('Lenticular cloud', 'a standing lens-shaped cloud at the crest of a mountain wave. It does not move, and it means strong winds'),
        ])

# ===================================================================
# I.D & I.E — VFR MINIMUMS, PERSONAL MINIMUMS
# ===================================================================

VFRMIN = ("OralVFRMins", "VFR Minimums — The Full Table", "91.155",
          "Your guide has “VFR triangle?” and “Define LIFR, IFR, MVFR and VFR” as headings with nothing under them. Here is the complete 91.155 table, not a summary — every row, because the examiner picks the row and you do not get to choose which.",
        [
 d('Class A', 'not applicable. There is no VFR in Class A'),
 d('Class B', '3 statute miles, and CLEAR OF CLOUDS. The only class with no distance figures at all — because ATC is separating everyone in there'),
 d('Class C', '3 SM. 500 below, 1,000 above, 2,000 horizontal'),
 d('Class D', '3 SM. 500 below, 1,000 above, 2,000 horizontal'),
 d('Class E, below 10,000 MSL', '3 SM. 500 below, 1,000 above, 2,000 horizontal'),
 d('Class E, at or above 10,000 MSL', '5 SM. 1,000 below, 1,000 above, 1 STATUTE MILE horizontal'),
 d('Class G, day, 1,200 AGL or less', '1 SM, clear of clouds'),
 d('Class G, night, 1,200 AGL or less', '3 SM. 500 below, 1,000 above, 2,000 horizontal'),
 d('Class G night, the pattern exception', 'within half a mile of the runway, in the traffic pattern of an airport with visible lights: 1 SM and clear of clouds'),
 d('Class G, above 1,200 AGL but below 10,000 MSL, day', '1 SM. 500 below, 1,000 above, 2,000 horizontal'),
 d('Class G, above 1,200 AGL but below 10,000 MSL, night', '3 SM. 500 below, 1,000 above, 2,000 horizontal'),
 d('Class G, above 1,200 AGL AND at or above 10,000 MSL', '5 SM. 1,000 below, 1,000 above, 1 statute mile horizontal'),
 d('The 10,000 rule needs BOTH', 'at or above 10,000 MSL AND more than 1,200 AGL before you jump to 5 SM and 1,000/1,000/1. Dropping the AGL half is the standard error'),
 d('LIFR', 'ceiling below 500 feet AGL, and/or visibility below 1 statute mile'),
 d('IFR', 'ceiling 500 to less than 1,000 feet AGL, and/or visibility 1 to less than 3 statute miles'),
 d('MVFR', 'ceiling 1,000 to 3,000 feet AGL, and/or visibility 3 to 5 statute miles'),
 d('VFR', 'ceiling greater than 3,000 feet AGL, and visibility greater than 5 statute miles'),
 d('And / or', 'every one of those four is and/or. The WORSE of ceiling and visibility decides the category — a 4,000-foot ceiling with 2 miles is IFR, not VFR'),
        ])

PERSMIN = ("OralPersonalMins", "Personal Minimums", "The Empty Heading",
           "Another heading in your guide with no answer under it. The ACS grades Risk Management on whether you HAVE a personal standard, not on whether you can recite 91.155 — so this is a question you answer with your own numbers, and the examiner will ask for them.",
        [
 d('What they are', 'limits stricter than the FAR that you write down while you are calm on the ground, so that you are not negotiating with yourself in the air'),
 d('Why they exist', 'the regulation is a floor for every pilot in the country. It says nothing about YOUR currency, YOUR aircraft or YOUR experience today'),
 d('The five areas', 'ceiling and visibility; wind and crosswind; day versus night; terrain, airport and runway; and your own condition'),
 d('Ceiling and visibility', 'set a number above 91.155 and above what you have actually flown in recently. The FAA worksheet starts from your recent training and adds a margin'),
 d('Crosswind', 'start BELOW the demonstrated crosswind in the POH, and raise it only after you have flown that number with an instructor. Demonstrated is a test-pilot figure, not a limit and not a target'),
 d('Runway', 'a minimum length, and a percentage added to the POH takeoff and landing distances — the book numbers come from a new aeroplane and a test pilot'),
 d('Experience', 'tighten everything for an unfamiliar aircraft, an unfamiliar airport, or a long layoff. Any one of those is a reason to move a number, never a reason to move it the other way'),
 d('The one rule', 'you may adjust them on the GROUND, deliberately, and never in the air and never on the day of the flight in the direction that suits you'),
 d('How to answer it', 'give your actual numbers. “I have not written any” is a Risk Management failure; a number you can defend is the whole point'),
        ])

# ===================================================================
# I.F — WEIGHT & BALANCE, TURNING TENDENCIES, WAKE
# ===================================================================

CG = ("OralCG", "Weight, Balance & CG", "The Two Empty Headings",
      "Your guide asks what a forward or aft CG does and what an overloaded aeroplane does, and answers neither. Both come up on every checkride, and the aft-CG answer is the one with teeth.",
        [
 d('The equation', 'Weight × Arm = Moment. CG = total moment ÷ total weight'),
 d('Datum', 'an arbitrary reference point chosen by the manufacturer. Every arm is measured from it, so the datum is the first thing you find in Section 6'),
 d('Forward CG', 'MORE stable in pitch, HIGHER stall speed, longer takeoff roll, slower cruise, heavier elevator forces — and harder to flare'),
 d('Aft CG', 'LESS stable, lower stall speed, shorter takeoff roll, slightly faster cruise, and light, twitchy pitch. A spin becomes harder, or impossible, to recover from'),
 d('Which one is dangerous', 'aft. A forward CG makes the aeroplane heavy and dull; an aft CG can make it unrecoverable. If you must be outside, be outside forward'),
 d('Why a forward CG raises the stall speed', 'the tail has to push down harder to balance it, and the wing carries that extra download as well as the weight. More lift required means the critical angle comes at a higher speed'),
 d('Overloaded', 'higher takeoff speed, longer takeoff run, reduced rate AND angle of climb, lower ceiling, shorter range, reduced manoeuvrability, higher stall speed, higher landing speed and a longer landing roll'),
 d('The two limits are independent', 'you can be under gross and outside the envelope, or inside the envelope and over gross. Check BOTH, every time'),
 d('Useful load', 'maximum ramp weight minus basic empty weight — fuel, occupants and baggage. PAYLOAD is the same thing without the fuel'),
 d('Ramp versus takeoff weight', 'the difference is the fuel burned taxiing and running up. Small, but it is why the two numbers exist'),
 d('Basic empty weight', 'airframe, engine, unusable fuel, and FULL operating fluids including full engine oil. The oil catches people'),
        ])

TURN = ("OralTurning", "The Four Turning Tendencies", "The Empty Heading",
        "Listed in your guide as a question with no answer. All four push the nose the SAME way, which is the answer to “why right rudder” — and the examiner usually wants all four names plus when each one bites.",
        [
 d('Torque', 'the propeller turns clockwise seen from the cockpit, so the airframe is pushed anticlockwise — a ROLL to the left. Greatest at high power and low airspeed'),
 d('P-factor', 'at a high angle of attack the descending RIGHT blade takes a bigger bite than the ascending left one, so thrust is asymmetric and the nose YAWS left. Climbs and slow flight'),
 d('Gyroscopic precession', 'the propeller is a gyroscope: a force applied at one point acts 90 degrees later in the direction of rotation. Raise the tail on the takeoff roll and the yaw comes out LEFT'),
 d('Spiralling slipstream', 'the corkscrew of air off the propeller strikes the LEFT side of the vertical fin, pushing the tail right and the nose left. Most noticeable at high power and low speed'),
 d('All four go LEFT', 'which is why the fin is offset, why there is a rudder trim tab, and why you need RIGHT rudder on every climb'),
 d('When they are worst', 'high power, low airspeed, high angle of attack — takeoff, the initial climb and slow flight. Exactly the three places you have least margin'),
 d('Which one is NOT one of them', 'overbanking tendency. That is the faster outer wing in a turn, it happens at any power setting, and it is held off with opposite aileron — a different effect entirely'),
 d('The one-line answer', 'torque rolls you, P-factor and slipstream yaw you, precession yaws you when the pitch attitude changes. Right rudder answers all four'),
        ])

WAKE = ("OralWake", "Wake Turbulence", "Avoidance",
        "The guide gives the technique in one line — stay above the flight path, three whites on the PAPI. These are the cases behind it, and the rule flips depending on whether the aeroplane ahead is departing or arriving.",
        [
 d('What it is', 'counter-rotating vortices trailing from the wingtips. It is the by-product of producing lift, so it starts at rotation and stops at touchdown'),
 d('The worst case', 'HEAVY, CLEAN and SLOW — a large aircraft just after rotation, or on final with the flaps up. That is when the vortices are strongest'),
 d('They sink', 'about 300 to 500 fpm below the flight path, levelling off roughly 900 feet beneath it. So the safe place is ABOVE'),
 d('In light or calm wind', 'they drift outward along the ground, and can settle onto a parallel runway or hold the vortex over the runway you are using'),
 d('Departing behind a large aircraft', 'rotate BEFORE its rotation point and stay ABOVE its climb path'),
 d('Landing behind a large landing aircraft', 'stay ABOVE its approach path and touch down BEYOND its touchdown point'),
 d('Landing behind a large DEPARTING aircraft', 'land WELL BEFORE its rotation point — the opposite of the rule above, because there is no wake before it rotates'),
 d('Departing behind a large landing aircraft', 'lift off BEYOND its touchdown point, for the same reason in reverse'),
 d('On the PAPI', 'three whites keeps you above the path. That is the practical version of every rule above'),
 d('Helicopters', 'avoid them too. The downwash from a hovering helicopter can exceed the wake of a fixed-wing of similar weight'),
 d('Who is responsible', 'ATC applies separation — but a VFR pilot who accepts a visual approach or a “caution wake turbulence” accepts responsibility for their own spacing'),
        ])

# ===================================================================
# I.H — AERONAUTICAL DECISION MAKING
# ===================================================================
# DECIDE and the 3P family used to be five lines buried at the end of the
# Hazardous Attitudes bank, which is a bank about something else. Your guide
# gives DECIDE its own heading ("Acronym for ADM during flight") and a
# separate "ADM & Risk Management" section, so it gets its own topic here.
# PAVE, IMSAFE and NWKRAFT are NOT restated \u2014 they have a parent already.

ADM = ("OralADM", "Decision Making \u2014 DECIDE & 3P", "ADM & Risk Management",
       "Two models, and the examiner wants to hear that you know WHEN each one applies \u2014 DECIDE when something has already changed, 3P before it does. Everything else here hangs off those two.",
        [
 d('DECIDE', 'Detect, Estimate, Choose, Identify, Do, Evaluate. Six steps, and the last one feeds straight back into the first'),
 d('D \u2014 Detect', 'that a change has occurred. Naming it out loud is the step people skip, and skipping it is how a pilot keeps flying the old plan'),
 d('E \u2014 Estimate', 'the need to counter or react to that change'),
 d('C \u2014 Choose', 'a desirable outcome for the flight'),
 d('I \u2014 Identify', 'the actions that will control the change'),
 d('D \u2014 Do', 'take the action'),
 d('E \u2014 Evaluate', 'the effect of the action \u2014 then run the loop again'),
 d('When DECIDE applies', 'REACTIVE. Something has already changed and you are responding to it in flight'),
 d('3P', 'Perceive, Process, Perform. PROACTIVE \u2014 run before and throughout the flight to find hazards before they change anything'),
 d('Perceive uses', 'PAVE \u2014 Pilot, Aircraft, enVironment, External pressures'),
 d('Process uses', 'CARE \u2014 Consequences, Alternatives, Reality, External pressures'),
 d('Perform uses', 'TEAM \u2014 Transfer, Eliminate, Accept, Mitigate'),
 d('Hazard versus risk', 'a HAZARD is the condition itself \u2014 a low ceiling, a short runway, a tired pilot. RISK is how likely it is to hurt you and how badly. PAVE finds hazards; CARE turns them into risk'),
 d('The risk matrix', 'likelihood \u2014 probable, occasional, remote, improbable \u2014 plotted against severity \u2014 catastrophic, critical, marginal, negligible'),
 d('SRM', 'Single-Pilot Resource Management: using every resource you have when there is nobody in the right seat. Single-pilot does not mean alone'),
 d('The six SRM elements', 'aeronautical decision-making, risk management, task management, automation management, situational awareness, and CFIT awareness'),
 d('The 5P check', 'Plan, Plane, Pilot, Passengers, Programming \u2014 run at preflight, pre-takeoff, hourly en route, pre-descent and before the approach'),
 d('Why five fixed points', 'a check you run once is a preflight, not a decision model. The schedule is what makes it work'),
 d('Situational awareness', 'an accurate picture of the aircraft, the environment and yourself \u2014 and what all three will be doing next. Losing it is the common thread through most ADM accidents'),
 d('Current versus proficient', 'current is the FAA legal minimum and means you may go. Proficient means you can fly it well TODAY. The examiner asks so they hear that you know the difference'),
        ])

# ===================================================================
# MCQ — THE CHECKRIDE
# ===================================================================

CHKQ = [
 ("The ACS code PA.I.B.K3 appears on your knowledge test report. What does it tell you?",
  ["Private Airplane, Area of Operation I, Task B, Knowledge element 3 — Airworthiness Requirements.",
   "Private Airplane, page 1, section B, question 3.",
   "A Risk Management element in Area I, since K codes are risk codes."],
  "The code is an address: certificate and category, then Area, then Task, then the element type and number. K is Knowledge, R is Risk Management, S is Skill. Area I Task B is Airworthiness Requirements, so a missed K3 there tells you exactly what the examiner is obliged to re-test — your report is a published question list."),
 ("Which Task in Area I does NOT apply to your ASEL checkride?",
  ["Task I.I — it covers seaplane and water characteristics.",
   "Task I.H — Human Factors, which is covered on the knowledge test instead.",
   "Task I.F — Performance and Limitations, which is tested in flight."],
  "Area I runs A through I, and the last one is seaplane-only, as is Task II.E (Taxiing and Sailing). Everything else in Areas I and II applies to you. Human Factors and Performance are both very much in the oral — Human Factors in particular is a full Task, not a footnote."),
 ("The examiner hands you the maintenance logbooks. What kind of ACS element is that?",
  ["A SKILL element — Task I.B asks you to determine the aeroplane is airworthy from the records provided.",
   "A Knowledge element, since it is asked on the ground.",
   "A Risk Management element, since it concerns airworthiness."],
  "People assume the ground portion is all Knowledge. It is not: Task I.B carries a Skill element, and the examiner must cover ALL Skill elements. It is graded as a demonstration, not a recitation — you open the books, find the dates and tach times, and walk them through the AD list."),
 ("You arrive for the checkride without your Airman Knowledge Test Report. What happens?",
  ["The test cannot begin — it is a required document and the examiner tests the codes you missed.",
   "The examiner looks it up in IACRA and the test continues.",
   "You may proceed, but you forfeit credit for the knowledge test."],
  "It is on the FAA's own document list in FAA-G-ACS-2, and it drives part of the Plan of Action, so there is no test without it. Bring the original. The other easily-forgotten item is a previous Notice of Disapproval or Letter of Discontinuance, if you have one."),
 ("Who acts as pilot in command during the practical test?",
  ["You do — the applicant is PIC for the entire flight.",
   "The examiner, who holds the higher certificate.",
   "Neither — the flight is conducted as dual instruction."],
  "You are PIC, you provide an airworthy aeroplane, and you make the go/no-go decision — including the decision to discontinue for weather. That is not a formality: an examiner who sees you defer the decision to them has learned something about your risk management before the engine starts."),
 ("What does 61.45 require of the aeroplane that an ordinary rental might not have?",
  ["Two pilot stations with engine and flight controls easily reached and operable in a conventional manner by BOTH pilots.",
   "A current 100-hour inspection in addition to the annual.",
   "An operable autopilot."],
  "61.45 also wants US registry, the right category and class, a standard (or limited, primary or light-sport) airworthiness certificate, adequate visibility for both seats, and no operating limitation that prohibits a required Area of Operation. An aeroplane with limiting characteristics produces a limitation printed on your certificate."),
 ("The test is discontinued for weather after you have passed the oral. What happens to that credit?",
  ["You keep credit for every Area of Operation already passed, and complete the remainder within 60 days.",
   "You keep the credit indefinitely until you choose to return.",
   "You lose the credit and repeat the whole test."],
  "61.43 preserves the credit and 61.43(f)(1) starts a 60-day clock from the date of discontinuance. Two catches worth saying out loud: a Letter of Discontinuance does NOT extend your knowledge test report, and if the examiner doubts your competence in an area you were credited with, they may re-examine it anyway."),
 ("What did FAA-S-ACS-6C replace?",
  ["The Private Pilot Practical Test Standards — entirely, for this certificate.",
   "Nothing — the ACS supplements the PTS, which is still the grading document.",
   "Only the knowledge test standards; the PTS still governs the flight."],
  "The ACS replaced the PTS outright and folded the knowledge-test and practical-test standards into one document. That is the structural point behind the whole system: the question you missed on the written and the Task you fly are addressed by the same code, which is what lets the examiner build the Plan of Action from your report."),
 ("A Letter of Discontinuance gives you 60 days. What does it NOT do?",
  ["It does not extend the expiry of your knowledge test report.",
   "It does not preserve credit for Areas of Operation you passed.",
   "It does not have to be brought back for the continuation."],
  "If the written expires inside those 60 days, the 60 days do not save you — two independent clocks, and the shorter one wins. It DOES preserve your credit, and you DO bring the original form back, along with any additional training endorsement and a new signed application."),
 ("You failed one Area of Operation. What must happen before you can retest?",
  ["Additional training from an authorised instructor, plus an endorsement saying you received it.",
   "A mandatory 30-day waiting period.",
   "Retaking the knowledge test."],
  "Training plus the endorsement, and the instructor completes the Instructor's Recommendation block on the application. There is no waiting period at the private pilot level, and the knowledge test stands as long as it is inside its 24-calendar-month window — both of those are requirements people expect to exist and invent for themselves."),
]

# ===================================================================
# MCQ — WEATHER
# ===================================================================

WXQ = [
 ("What two conditions must both exist for structural icing to form?",
  ["Visible moisture, and an aircraft surface temperature at or below 0 Celsius.",
   "An outside air temperature below 0 Celsius, and relative humidity above 80 percent.",
   "Visible moisture, and flight in cloud."],
  "Both, and the temperature that matters is at the COLLECTING SURFACE, not on the OAT gauge — which is why ice can form with the OAT a little above zero. Take either ingredient away and you have no ice, which is also the escape: leave the visible moisture, or get to air where the surface stays warm."),
 ("Large water drops freezing slowly across the airframe produce which kind of ice?",
  ["Clear ice — a smooth, heavy sheet, and the hardest to shed.",
   "Rime ice — opaque and rough.",
   "Frost — deposition straight from vapour to ice."],
  "Slow freezing lets the water run back before it sets, so it spreads as a smooth heavy layer. Small drops freezing FAST trap air and give rime — rough, milky and lighter. Both at once is mixed. Frost is not an in-flight icing type at all: it is deposition, vapour straight to ice, on a parked aeroplane."),
 ("How does structural icing affect the aircraft?",
  ["It destroys lift, adds weight and drag, and can jam a control — raising the stall speed while cutting available power.",
   "It adds weight, which is the primary hazard; the aerodynamic effect is minor.",
   "It reduces cruise speed but does not affect stall speed."],
  "The aerodynamic effect dominates the weight. Disrupted airflow separates early, so you need a higher speed to stay flying at the moment the propeller and the engine are losing efficiency to the same ice. Both ends of the margin close at once, which is why the answer is always to leave the conditions rather than manage them."),
 ("Why is frost on the wings hazardous?",
  ["Its roughness spoils the smooth airflow and causes early separation, so you may not get airborne at all.",
   "Its weight reduces the useful load below the takeoff requirement.",
   "It melts in flight and refreezes as clear ice on the control surfaces."],
  "It is about texture, not mass — a layer too thin to weigh anything can cost enough lift to stop the aeroplane flying off the runway. That is why the rule is remove it, not account for it. Polishing it smooth is not acceptable either: the FAA wants it off."),
 ("Which three conditions are required for a thunderstorm to form?",
  ["Sufficient water vapour, an unstable lapse rate, and an initial lifting force.",
   "High humidity, a cold front, and surface heating.",
   "Cumulus clouds, wind shear, and a temperature inversion."],
  "Moisture, instability, lift. A front is one possible lifting force, but so is terrain, so is convergence, and so is heating from below — which is why a thunderstorm can build in an unstable air mass with no front anywhere near it. Name the mechanism, not one example of it."),
 ("At which stage of a thunderstorm are the hazards greatest?",
  ["The mature stage — it begins when precipitation reaches the ground.",
   "The cumulus stage, when the updraft is building fastest.",
   "The dissipating stage, when the downdraft dominates."],
  "Precipitation at the surface marks the start of the mature stage, and it is the stage with BOTH updraft and downdraft running — over 6,000 fpm up and over 2,500 down, side by side. The cumulus stage is updraft only and the dissipating stage is downdraft only; it is the pair together that tears an aeroplane apart."),
 ("Which is true of a microburst?",
  ["Less than 2.5 miles across, with downdrafts to 6,000 fpm, and peak winds lasting under 5 minutes.",
   "Typically 10 to 15 miles across, lasting around 30 minutes at peak intensity.",
   "It can form in any cloud type, including stratus."],
  "Small, violent and short — though a SEQUENCE of them can run over 30 minutes, which is why one having passed is not clearance to go. Convective activity only, and the mature stage only. The size is what makes it dangerous: it is too small to see and too short to forecast."),
 ("Flying an approach you meet an increasing headwind and the aircraft rises above the glide path. What should you suspect?",
  ["A microburst — the performance-increasing side comes FIRST, and the downdraft and tailwind follow.",
   "Normal wind gradient; reduce power and re-establish the path.",
   "An updraft from surface heating, which is not hazardous."],
  "The trap is built into the phenomenon: the first thing it does is make the aeroplane perform better, so the instinct is to pull the power back — and that is the configuration you are in when the downdraft and then the tailwind arrive. Treat an unexplained performance INCREASE on short final as a reason to go around."),
 ("Where are the three areas of special concern for wind shear?",
  ["With a low-level temperature inversion, in a frontal zone or thunderstorm, and as CAT near a jet stream.",
   "Only in and around thunderstorms.",
   "On any approach with a crosswind over 15 knots."],
  "The inversion one is the one pilots forget, because the air under an inversion is smooth and stable and feels benign — the shear is at the BOUNDARY, not in the layer. That is the same boundary that traps the fog and haze you are looking through on the approach."),
 ("What are the characteristics of a temperature inversion?",
  ["Smooth stable air close to the ground, with fog, stratus or haze underneath and turbulence and shear at the boundary.",
   "Turbulent unstable air with good visibility and cumulus development.",
   "Rapid cooling with height, above the standard 2 degrees per 1,000 feet."],
  "An inversion is temperature RISING with height, which is the opposite of standard, and it caps the air below it like a lid — so moisture and pollutants collect and the visibility goes. Clear cool nights and frontal boundaries are where you find them."),
 ("Which fog type REQUIRES wind to form?",
  ["Advection fog — warm moist air has to be moved over a cold surface.",
   "Radiation fog, which needs wind to mix the cooled air upward.",
   "Upslope fog, which needs wind to lift the air."],
  "Advection needs the wind to bring the air; radiation fog needs the opposite — calm, clear and a cooling surface, and wind breaks it up. Upslope needs air moving up a slope, so it needs wind too, but the discriminator the examiner is testing is radiation versus advection, and wind is what tells them apart."),
 ("Cold dry air moving over warm water produces which fog, and why does it matter?",
  ["Steam fog — and it comes with low-level turbulence AND icing.",
   "Advection fog — and it usually burns off by mid-morning.",
   "Radiation fog — and it is confined to the shoreline."],
  "It is the only one of the four formed by ADDING moisture rather than cooling the air, and the mechanism that makes it — cold unstable air over a warm surface — is also what makes it turbulent, with icing in the cold air above. That combination is why it is the worst of the four to fly through."),
 ("AIRMET Tango covers which conditions?",
  ["Moderate turbulence, sustained surface winds of 30 knots or more, and non-convective low-level wind shear.",
   "Moderate icing and freezing level heights.",
   "IFR conditions and extensive mountain obscuration."],
  "Tango turbulence, Sierra IFR and mountain obscuration, Zulu icing and freezing levels — and all three are MODERATE, valid 6 hours. The surface wind and the low-level wind shear riding along inside Tango is the half people drop; it is not a pure turbulence product."),
 ("How does a SIGMET differ from a Convective SIGMET?",
  ["A SIGMET covers severe NON-convective weather for up to 4 hours; a Convective SIGMET covers thunderstorm activity for 2.",
   "A SIGMET is for light aircraft only; a Convective SIGMET is for all aircraft.",
   "They are the same product issued by different offices."],
  "Non-convective versus convective is the split. A SIGMET means severe icing, severe or extreme turbulence or CAT not associated with thunderstorms, and dust or sandstorms below 3 SM. A Convective SIGMET is issued at 55 past the hour, valid 2 hours, for surface winds of 50 knots or more, hail 3/4 inch or larger, tornadoes, or embedded thunderstorms."),
 ("A Convective SIGMET has been issued. What does it imply without saying so?",
  ["Severe or greater turbulence, severe icing, and low-level wind shear.",
   "Moderate turbulence and moderate icing.",
   "Nothing beyond what is written in the text."],
  "All three are implied automatically by the product itself, which is why the text does not list them. Practically it means a Convective SIGMET is not something you plan around by a few miles — the AIM asks for 20 NM from a severe or heavy-precipitation thunderstorm, and hazardous turbulence reaches 20 miles from the radar echo edge."),
 ("The winds aloft forecast reads 731960. Decode it.",
  ["230 degrees at 119 knots, minus 60 Celsius.",
   "073 degrees at 19 knots, plus 60 Celsius.",
   "230 degrees at 19 knots, minus 60 Celsius."],
  "A direction over 36 means 50 was added and 100 subtracted from the speed: 73 minus 50 gives 230 degrees, 19 plus 100 gives 119 knots. Temperature is minus 60. A speed of 199 or more is coded 99, so 7799 is 270 at 199 or more; 9900 is light and variable, under 5 knots."),
 ("Above 24,000 feet the winds aloft forecast omits the minus sign on the temperature. Why?",
  ["Above that altitude the temperature is always negative, so the sign carries no information.",
   "Temperatures above 24,000 feet are reported in Fahrenheit instead.",
   "The forecast omits temperature entirely above 24,000 feet."],
  "It is a coding economy, not a special case. Two other coding rules worth having with it: there is no wind forecast within 1,500 feet of the station elevation, and no temperature within 2,500 feet of it — which is why the lowest levels are often blank for a nearby station."),
 ("You fly from a high pressure area to a low pressure area without updating the altimeter setting. What happens?",
  ["The altimeter reads HIGHER than you actually are — so you are lower than it says.",
   "The altimeter reads lower than you actually are, giving you extra clearance.",
   "The altimeter is unaffected until you change altitude."],
  "High to low, look out below — and the same error comes from flying from WARM air into COLD. The mnemonic belongs to the cold, low-pressure case, and attaching it to the warm case is a common way to invert the whole answer. The instrument is reading a pressure that no longer corresponds to the altitude it is labelled with."),
 ("Temperature and dew point are within 5 degrees of each other. What should you expect?",
  ["Visible moisture — cloud, dew or fog — and ideal conditions for carburettor icing.",
   "Clear skies, since the air is not yet saturated.",
   "Turbulence, as the air is unstable."],
  "A converging spread is the single most useful number on a METAR for a VFR pilot, because it tells you what is about to happen rather than what is happening. The carburettor icing half of the answer is what makes it a systems question as well as a weather one — that is exactly when you start using carb heat proactively."),
 ("You are planning a flight for tomorrow morning. Which briefing do you ask for?",
  ["An Outlook briefing — it is for a departure 6 or more hours away.",
   "A Standard briefing, which is always the correct request.",
   "An Abbreviated briefing, since you will update it later."],
  "Outlook for planning, Standard before you go, Abbreviated to top it up. Asking for a Standard every time is not WRONG, but the examiner is checking that you know why the other two exist — and an Outlook explicitly does not give you current conditions, so it can never be your go/no-go."),
]

# ===================================================================
# MCQ — PERFORMANCE & AERODYNAMICS
# ===================================================================

PERFQ = [
 ("What does a forward CG do to the stall speed, and why?",
  ["It RAISES it — the tail must push down harder, and the wing carries that download as well as the weight.",
   "It lowers it, because the aircraft is more stable in pitch.",
   "It has no effect; stall speed depends only on weight."],
  "The tail is producing negative lift to balance the nose-down moment, so the wing has to lift the aeroplane PLUS that download. More required lift means the critical angle arrives at a higher speed. The same mechanism explains the rest of the forward-CG list: longer takeoff roll, slower cruise, heavier elevator and a harder flare."),
 ("Which CG position is the dangerous one, and why?",
  ["Aft — it reduces stability and can make a spin unrecoverable.",
   "Forward — it raises the stall speed and lengthens the takeoff roll.",
   "Neither; the envelope is equally safe at both ends."],
  "A forward CG makes the aeroplane heavy and dull to fly — unpleasant, not lethal. An aft CG makes it light, twitchy and progressively less willing to recover, and a spin entered behind the aft limit may not come out. If you must err, err forward."),
 ("An overloaded aeroplane suffers which combination?",
  ["Higher takeoff speed, longer run, reduced rate AND angle of climb, lower ceiling, higher stall and landing speeds.",
   "A longer takeoff run but an unchanged climb rate.",
   "Reduced range only; the handling is unaffected."],
  "Every number moves against you at once, which is the point of the question. Note rate AND angle of climb — people give up the rate and forget the angle, and the angle is what clears the trees at the end of a short strip on a hot day."),
 ("You are under maximum gross weight. Does that mean the aircraft is loaded legally?",
  ["No — weight and CG are independent limits and BOTH must be met.",
   "Yes, if you are under gross the CG is necessarily within the envelope.",
   "Yes, provided the baggage compartment limit is also respected."],
  "You can be light and out of the envelope, or in the envelope and over gross. The classic case is two people up front with full fuel and an empty back — nowhere near gross, and forward of the limit. Compute both, every flight, and know which one you are close to."),
 ("Which factor makes air LESS dense, contrary to what most people expect?",
  ["High humidity — water vapour is lighter than the air it displaces.",
   "Low temperature, because cold air sinks.",
   "High pressure, because the molecules are compressed."],
  "Damp air FEELS heavy, and it is lighter. Water vapour displaces nitrogen and oxygen molecules with a lighter one, so a humid day raises density altitude on top of whatever the temperature and elevation are already doing. The trio is altitude, temperature and humidity, all in the same direction."),
 ("Air density directly affects which four things?",
  ["Lift from the wing, power from the engine, propeller efficiency, and drag.",
   "Lift and drag only; the engine is unaffected in a normally aspirated aircraft.",
   "Engine power and propeller efficiency only."],
  "All four, and three of them move against you as density falls. That is why density altitude is not a wing problem or an engine problem but a whole-aeroplane problem, and why the takeoff distance chart and the climb chart both need it as an input."),
 ("Which altitude do you use as the entry to a performance chart?",
  ["Pressure altitude — set 29.92 in the window to read it directly.",
   "Indicated altitude with the local setting.",
   "Density altitude, read directly from the altimeter."],
  "Charts take pressure altitude and temperature, and they do the density-altitude conversion internally. Density altitude is what the aeroplane feels, but no altimeter reads it — which is why the rule of thumb matters: 1,000 feet per inch, and a setting BELOW 29.92 puts pressure altitude ABOVE field elevation."),
 ("On a hot day, what happens to your groundspeed at the same indicated airspeed?",
  ["It increases — thinner air means a higher true airspeed for the same indication.",
   "It decreases, because the aircraft has less power available.",
   "It is unchanged; indicated airspeed governs groundspeed."],
  "The airspeed indicator measures dynamic pressure, so in thin air the same indication means you are physically moving faster. The practical consequence is on landing: the same indicated approach speed puts you over the fence faster across the ground, and the landing roll grows accordingly."),
 ("All four turning tendencies push the aircraft in which direction?",
  ["Left — which is why right rudder is needed on every climb.",
   "Right, which the offset fin corrects for.",
   "They oppose each other and cancel out at cruise power."],
  "Torque, P-factor, gyroscopic precession and spiralling slipstream all go the same way in a US-built single, which is why the fin is offset and why there is a rudder trim tab. They are worst at high power, low airspeed and high angle of attack — takeoff, initial climb and slow flight."),
 ("When is P-factor at its strongest?",
  ["At a high angle of attack — in the climb and in slow flight.",
   "At high airspeed in level cruise.",
   "During the takeoff roll before the tail rises."],
  "P-factor needs the propeller disc tilted relative to the airflow, which is what a high angle of attack produces. The descending right blade then takes a bigger bite than the ascending left one and the nose yaws left. In level cruise the disc is nearly perpendicular to the airflow and P-factor all but disappears."),
 ("Gyroscopic precession applies a force how?",
  ["90 degrees later, in the direction of rotation.",
   "Directly opposite to the force applied.",
   "180 degrees later, in the direction of rotation."],
  "The propeller is a gyroscope, so a force applied at one point on the disc acts a quarter turn further round. Raising the tail on a takeoff roll applies a forward force at the top of the disc, which comes out as a yaw to the LEFT. It is most obvious in a taildragger but the same physics applies to any pitch change."),
 ("The spiralling slipstream causes a left yaw by striking what?",
  ["The LEFT side of the vertical fin, pushing the tail right.",
   "The right side of the vertical fin, pushing the tail left.",
   "The underside of the horizontal stabiliser."],
  "The corkscrew of air off the propeller wraps around the fuselage and arrives at the tail from the left, pushing the tail right and therefore the nose left. Most noticeable at high power and low speed — the same conditions as the other three, which is why they are taught together."),
 ("Why must you increase back pressure in a steep turn?",
  ["Banking splits lift into horizontal and vertical components, so the vertical component shrinks.",
   "The wings produce less lift at a high bank angle because of reduced airflow.",
   "To counteract the overbanking tendency of the outer wing."],
  "The wing is producing the same total lift; you have simply pointed some of it sideways, which is what turns you. Back pressure increases the angle of attack to restore the vertical component — and that extra lift is exactly why load factor and stall speed rise with bank. Overbanking is a separate effect, held off with opposite aileron."),
 ("At 60 degrees of bank in level flight, what is the load factor and what happens to stall speed?",
  ["2 G, and the stall speed rises by about 41 percent — the square root of 2.",
   "2 G, and the stall speed is unchanged because weight has not changed.",
   "1.5 G, and the stall speed rises by about 25 percent."],
  "Load factor is 1 over the cosine of the bank angle: cos 60 is 0.5, so 2 G. Stall speed scales with the SQUARE ROOT of load factor, so root 2 is 1.41 — a 41 percent increase. At 45 degrees it is 1.41 G and about 19 percent; at 75 degrees it is 3.86 G and nearly double the stall speed."),
 ("What causes an aeroplane to stall?",
  ["Exceeding the critical angle of attack — at any airspeed, weight or attitude.",
   "Flying below the published stall speed in the POH.",
   "Losing airspeed until the wing can no longer produce lift."],
  "It is an angle event, never a speed event. The published stall speed is just the speed at which, at max gross in 1 G unaccelerated flight, you happen to reach that angle. Load it up, bank it, or pull hard, and the same angle arrives a great deal faster — which is the whole basis of the accelerated stall."),
 ("What is ground effect and what does it do?",
  ["Within about one wingspan of the surface the ground interferes with wingtip vortices, cutting induced drag.",
   "A cushion of compressed air under the wing that supports the aircraft's weight.",
   "Increased lift caused by the higher air density near the surface."],
  "It is a DRAG reduction, not an air cushion — the ground stops the vortices forming fully, so induced drag falls and the aeroplane will lift off below its normal flying speed and float on landing. The trap is taking off in it with insufficient speed and settling back as you climb out of it."),
 ("Departing behind a large aircraft that has just taken off, what do you do?",
  ["Rotate BEFORE its rotation point and stay ABOVE its climb path.",
   "Rotate after its rotation point and climb beneath its path.",
   "Wait three minutes, after which the wake has dissipated."],
  "Wake starts at rotation and sinks 300 to 500 fpm below the flight path, so the clean air is behind-and-above the point where it started. Note the rule INVERTS for a landing aircraft: land beyond its touchdown point, because its wake stops there. Ahead of rotation and beyond touchdown — the two ends where there is no wake at all."),
 ("What does the demonstrated crosswind component in the POH actually mean?",
  ["The highest crosswind a test pilot demonstrated during certification — it is not a limitation.",
   "The maximum crosswind in which the aircraft may legally be operated.",
   "The crosswind at which the rudder reaches full deflection."],
  "It is a data point, not a limit and not a target: a factory pilot in a new aeroplane on a good day. Your own personal minimum should start well below it and move up only after you have flown that number with an instructor — which is exactly the answer an examiner is fishing for when they ask what your crosswind limit is."),
]

# ===================================================================
# ASSEMBLY
# ===================================================================

DEFS3 = [WXHAZ, VFRMIN, PERSMIN, CG, TURN, WAKE, ADM]

BANKS3 = [
    ("OralCheckrideQ", "The Checkride — Scenarios", CHKQ,
     [("How a checkride actually runs", "https://www.youtube.com/results?search_query=private+pilot+checkride+oral+exam+what+to+expect+DPE"),
      ("Reading the ACS and your test report codes", "https://www.youtube.com/results?search_query=airman+certification+standards+ACS+codes+knowledge+test+report+explained")]),
    ("OralWxQ", "Weather — Scenarios", WXQ,
     [("Icing, and what it does to the aeroplane", "https://www.youtube.com/results?search_query=structural+icing+clear+rime+mixed+ice+effects+explained+pilot"),
      ("Thunderstorm stages, microbursts and wind shear", "https://www.youtube.com/results?search_query=thunderstorm+life+cycle+microburst+wind+shear+explained+private+pilot"),
      ("The four types of fog", "https://www.youtube.com/results?search_query=four+types+of+fog+radiation+advection+upslope+steam+explained+pilot"),
      ("AIRMET, SIGMET and Convective SIGMET", "https://www.youtube.com/results?search_query=AIRMET+SIGMET+convective+SIGMET+difference+explained+private+pilot")]),
    ("OralPerfQ", "Performance & Aerodynamics — Scenarios", PERFQ,
     [("Weight and balance, forward and aft CG", "https://www.youtube.com/results?search_query=weight+and+balance+forward+aft+CG+effects+explained+private+pilot"),
      ("The four left-turning tendencies", "https://www.youtube.com/results?search_query=four+left+turning+tendencies+torque+P-factor+precession+slipstream+explained"),
      ("Density altitude and performance", "https://www.youtube.com/results?search_query=density+altitude+performance+charts+explained+private+pilot"),
      ("Wake turbulence avoidance", "https://www.youtube.com/results?search_query=wake+turbulence+avoidance+takeoff+landing+behind+large+aircraft")]),
]

MCQ_DESC3 = {
    'OralCheckrideQ': "The test about the test. How the ACS is addressed, what the examiner must cover, who is PIC, what 61.45 wants of the aeroplane, and what the two ways of ending it actually mean for your paperwork.",
    'OralWxQ': "Task I.C asked as scenarios. Every item here is an answer that exists in your guide — the two icing conditions, the three thunderstorm ingredients, the three wind-shear areas, the four fogs — turned into the situation the examiner builds around it.",
    'OralPerfQ': "Task I.F and the aerodynamics behind it, including the two questions your guide asks and leaves blank: what a forward or aft CG does, and what an overloaded aeroplane does. Plus the four turning tendencies and the load-factor arithmetic.",
}

# Where the new topics slot into the existing sub-sections.
INSERTS = {
    "The Checkride":                        ["OralCheckrideQ"],
    "I.C — Weather":                        ["OralWxHazards", "OralWxQ"],
    "I.D & I.E — Cross-Country & Airspace":  ["OralVFRMins", "OralPersonalMins"],
    "I.F — Performance":                    ["OralCG", "OralTurning", "OralWake", "OralPerfQ"],
    "I.H — Human Factors":                 ["OralADM"],
}
