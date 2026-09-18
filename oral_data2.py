# -*- coding: utf-8 -*-
"""Oral Exam, part 2 — built from Or's own oral prep guide
(“PPL Oral Exam Preparation Questions”, Liraz Bershadsky), which is organised
by ACS Area and Task. Everything here follows that guide's structure and its
WIFA-specific procedures, with FAA sources checked and the guide's stale or
loose figures corrected in place (flagged in the item text where it matters,
because he will be asked from the guide as written).

Nothing here duplicates a topic that already lives under PAVE — Risk
Management (ARROW, AV1ATE, A TOMATO FLAMES, FLAPS, NWKRAFT, IMSAFE, PAVE,
NOTAMTypes) or under Acronyms (ANDS, UNOS, SAFETY): one parent per topic.
"""

A = '➔'   # the separator the generator splits definition items on

def d(term, meaning):
    return '%s %s %s' % (term, A, meaning)

# ===================================================================
# I.A — PILOT QUALIFICATIONS
# ===================================================================

QUAL = ("OralQual", "Certificates & Currency", "Task I.A",
        "61.103 eligibility, 61.56 the flight review and 61.57 recency — the first block of the oral and the one where an examiner can end the test before you have said anything about the aeroplane.",
        [
 d('61.103 Eligibility', 'be 17; read, speak, write and understand English; hold a third-class medical or BasicMed; hold the ground and flight training endorsements; meet the 61.109 experience; pass the knowledge and practical tests'),
 d('61.103(j)', 'you must ALREADY hold a US student, sport or recreational pilot certificate. Private is an upgrade, not a standing start'),
 d('61.56 Flight review', 'every 24 calendar months — at least 1 hour of ground and 1 hour of flight with an authorised instructor. A new certificate or rating resets the clock'),
 d('61.57(a) Day passengers', '3 takeoffs and landings in the preceding 90 days, in the same category, class and type if a type rating is required'),
 d('61.57(b) Night passengers', '3 takeoffs and landings TO A FULL STOP in the preceding 90 days, flown between 1 hour after sunset and 1 hour before sunrise'),
 d('61.23 Medical, under 40', 'third class lasts 60 calendar months — the age that counts is your age on the DAY OF THE EXAM, not today'),
 d('61.23 Medical, 40 and over', 'third class lasts 24 calendar months'),
 d('61.60 Address change', '30 days to notify the FAA, and you may not exercise your privileges after those 30 days until you have'),
 d('61.53 Self-grounding', 'you may not act as PIC knowing of a medical condition that would stop you meeting the requirements for your medical. IMSAFE is how you run the check'),
 d('Current versus proficient', 'current means you have met the FAA minimum and are legal. Proficient means you can actually fly it well today. The examiner asks this to hear that you know they are different'),
        ])

PRIV = ("OralPrivileges", "Privileges & Limitations", "14 CFR 61.113",
        "What a private certificate lets you do and what it does not. The whole section turns on one idea: you may share costs, you may never profit, and the flight may never be the reason you were paid.",
        [
 d('The core limitation', 'no carrying passengers or property for compensation or hire, and no acting as PIC of an aircraft for compensation or hire'),
 d('Pro rata share', 'you may share the operating expenses — fuel, oil, airport expenditures and rental fees, and only those — but you may never pay LESS than your equal share'),
 d('Business or employment', 'you may fly in connection with a business or employment only when the flight is INCIDENTAL to it and you carry no passengers or property for compensation or hire'),
 d('Charity', 'you may fly a charitable, nonprofit or community event under 61.113(d), if the conditions there are met'),
 d('Search and rescue', 'you may be reimbursed for aircraft operating expenses directly related to search and location operations'),
 d('Aircraft salesman', 'with at least 200 hours logged you may demonstrate an aircraft in flight to a prospective buyer'),
 d('Towing', 'you may tow a glider or an unpowered ultralight, provided you meet 61.69'),
 d('Production flight test', 'you may act as PIC of a production flight test in a light-sport aircraft'),
 d('The test to apply', 'ask who benefited and who paid. If the flight itself is what somebody is paying for, you may not fly it as a private pilot'),
        ])

DOCS = ("OralDocs", "What You Carry", "Personal Documents",
        "The examiner opens with this, and it is the cheapest question on the test to lose. Note what is required to be ON you, what is merely required to be PRESENTED, and what stays in the logbook.",
        [
 d('Pilot certificate', '61.3(a) — in your personal possession or readily accessible in the aircraft'),
 d('Medical or BasicMed', 'the medical certificate, or under BasicMed your driver’s licence plus the paperwork in your logbook'),
 d('Photo identification', '61.3(a)(2) — government-issued, with your photograph and signature. A passport or a driver’s licence'),
 d('Radiotelephone permit', 'the FCC restricted radiotelephone operator permit, and only for flights OUTSIDE the United States. Same rule as the second R in ARROW'),
 d('Your logbook', 'NOT a carriage item for a private pilot. 61.51(i) makes you PRESENT it on reasonable request, which is a different thing'),
 d('Student pilot', 'carries the logbook, the student pilot certificate and the endorsements on all SOLO CROSS-COUNTRY flights'),
 d('Sport pilot', 'carries evidence of the endorsements on EVERY flight. A recreational pilot only on certain solo flights — the three are not the same rule'),
 d('BasicMed paperwork', 'both the completed medical examination checklist, FAA Form 8700-2, and the course completion certificate, available in your LOGBOOK'),
        ])

BASICMED = ("OralBasicMed", "BasicMed (Part 68)", "Check Your Guide On This",
            "Your printed guide lists 5 passengers, 6,000 pounds and 6 occupants. Those are the ORIGINAL 2017 figures and they were raised by the 2024 FAA reauthorisation. Learn the current ones — the old numbers still appear in a great deal of study material, which is exactly what makes them a good distractor.",
        [
 d('Occupants', 'the aircraft must be authorised to carry not more than 7 occupants (it was 6)'),
 d('Weight', 'maximum certificated takeoff weight not more than 12,500 pounds (it was 6,000)'),
 d('Passengers', 'not more than 6 passengers may be carried (it was 5)'),
 d('Altitude', 'not above 18,000 feet MSL — effectively the bottom of Class A, which is a useful way to hold it'),
 d('Speed', 'not faster than 250 knots indicated'),
 d('Where', 'within the United States, or abroad only with that country’s authorisation'),
 d('Not for hire', 'the flight may not be for compensation or hire'),
 d('The exam', 'FAA Form 8700-2 with ANY state-licensed physician, every 48 calendar months. No FAA designation is required — and an Aviation Medical Examiner is a state-licensed physician too, so your usual AME may perform one'),
 d('The course', 'the online medical education course, every 24 calendar months. Two different clocks'),
 d('Your driver’s licence', 'must be valid, and you must comply with every restriction on it. If it says corrective lenses, so does your flying'),
        ])

# ===================================================================
# I.B — AIRWORTHINESS
# ===================================================================

INSP = ("OralInspections", "Inspections & Who Signs", "Task I.B",
        "The difference between the annual and the 100-hour is not what is checked — Part 43 Appendix D is the same scope list for both. It is WHO may sign it and WHAT triggers it.",
        [
 d('Annual', 'every 12 calendar months, for EVERY aircraft. Only an A&P holding an Inspection Authorisation may sign it off'),
 d('100-hour', 'only when carrying persons for hire, or giving flight instruction for hire in an aircraft the instructor provides — which describes a school aeroplane exactly. Any A&P may sign it; no IA needed'),
 d('The scope', 'Part 43 Appendix D lists what is inspected, and it is the same list for both'),
 d('The 10-hour overrun', '91.409(b) — you may exceed the 100 hours by up to 10 only while EN ROUTE to the place of inspection, and the excess counts against the next 100. It is not a grace period'),
 d('Substitution', 'an annual can stand in for a 100-hour. A 100-hour can NEVER stand in for an annual — the traffic only runs one way, because of who signs'),
 d('Who keeps it airworthy', '91.403 — the owner or operator, and that includes AD compliance'),
 d('Who decides on the day', '91.7(b) — the PIC determines the aircraft is in condition for safe flight, and shall DISCONTINUE the flight when an unairworthy condition occurs'),
 d('Special flight permit', '21.197 — a ferry permit to fly an out-of-annual aircraft to where the work can be done. Every AD that is DUE must still be complied with first'),
        ])

MAINT = ("OralMaint", "Maintenance & Paperwork", "AD, SB and the Records",
        "Proving airworthiness from the books is an ACS SKILL element, not a knowledge one — the examiner hands you the logbooks and watches you find it.",
        [
 d('Airworthiness Directive', 'a mandatory FAA regulation issued under Part 39 addressing an unsafe condition. Like a car recall, except you may not fly until it is complied with'),
 d('Service Bulletin', 'the manufacturer’s recommendation. Advisory only — unless an AD adopts it, at which point it becomes law'),
 d('Who ensures AD compliance', 'the owner or operator. The records must show every applicable AD, one-time and recurring'),
 d('Airworthiness certificate', 'no expiry date. Valid as long as the required inspections and maintenance are kept up. 91.203(b) requires it DISPLAYED at the cabin or cockpit entrance'),
 d('Registration certificate', 'expires 7 years after the last day of the month of issue. Must be carried aboard, but need not be displayed'),
 d('Preventive maintenance', '43.3(g) lets a certificated pilot do the jobs on the closed list in Part 43 Appendix A(c) on an aircraft they own or operate, when it is not run under Part 121, 129 or 135'),
 d('The log entry', '43.9 — a description of the work, the date completed, and your name, signature, certificate number and kind of certificate. It goes in the AIRCRAFT records, not your flight logbook'),
 d('Airworthy means two things', 'it conforms to its type certificate, AND it is in condition for safe operation. Inspections are how you evidence that, not the definition of it'),
        ])

POHEQ = ("OralPOH", "The POH & Equipment List", "Inoperative Equipment",
         "Straight from your guide, and it is the question that separates a recited 91.213 from someone who has actually opened Section 6.",
        [
 d('Matching the POH to the aeroplane', 'each POH belongs to ONE serial number. Check it against the registration certificate and the data plate on the airframe'),
 d('Section 6', 'the equipment list. This is where you find out whether a given item is required on YOUR aircraft'),
 d('The Cessna code', 'an "-R" against an item in the equipment list means REQUIRED. So the engine spinner is required on a Cessna and you may not go without it — on some other types you can. Look it up, do not assume'),
 d('KOEL', 'Kinds of Operation Equipment List, in the POH — what must work for day VFR, night VFR and each other kind of operation'),
 d('MEL', 'an FAA-APPROVED list specific to that aircraft and operator, and it becomes a supplemental type certificate. Once you have one you use it, and 91.213(d) no longer applies'),
 d('The 91.213(d) order', 'MEL if there is one; then the KOEL; then 91.205 (A TOMATO FLAMES, plus FLAPS at night); then a pilot or mechanic determination that it is not a hazard'),
 d('If you go', 'DEACTIVATE or REMOVE the item, and PLACARD it INOPERATIVE. Both actions, not one'),
 d('Seat belts', 'crew: belt and shoulder harness for taxi, takeoff and landing, belt only en route while at the station. Passengers: belted for taxi, takeoff and landing'),
 d('Over water for hire', 'beyond power-off gliding distance from shore, 91.205(b)(12) adds a flotation device for each occupant and at least one pyrotechnic signalling device'),
        ])

# ===================================================================
# I.C — WEATHER
# ===================================================================

WXSRC = ("OralWxSources", "Where Weather Comes From", "Task I.C",
         "Big picture to small picture — that is the order your guide gives and the order the examiner wants to hear you work in.",
        [
 d('Flight Service', '122.2 is the common FSS frequency nationwide, and 1800wxbrief.com is the web front end'),
 d('Aviation Weather Center', 'aviationweather.gov — including the GFA, the Graphical Forecasts for Aviation tool'),
 d('FIS-B', 'METAR, TAF, NEXRAD, AIRMET, SIGMET and convective SIGMET, TFRs, special use airspace, NOTAMs and PIREPs — in the cockpit, free, over ADS-B In'),
 d('In the air', 'FSS on 122.2, ATC, ASOS or AWOS, ATIS, and FIS-B'),
 d('Standard briefing', 'the complete picture. What you ask for before you go'),
 d('Abbreviated briefing', 'to update or supplement a briefing you already had, or after a delay'),
 d('Outlook briefing', 'when departure is 6 or more hours away. A PLANNING tool — it gives an initial forecast, not current conditions, so it is never your go/no-go'),
 d('PIREP', 'the only real-time report of turbulence, icing and cloud tops. Read the AIRCRAFT TYPE first — moderate turbulence in a 172 is not moderate in a 737'),
 d('Filing a PIREP', 'through FSS, en route ATC, or the control tower. The examiner likes hearing that you would file one, not just read one'),
        ])

WXPROD = ("OralWxProducts", "The Forecast Products", "AIRMET / SIGMET / Charts",
          "Three advisories and five charts. Hold the validity periods and the letters — that is what gets asked, and the T/S/Z split maps neatly onto the SIGMET criteria.",
        [
 d('AIRMET (WA)', 'valid 6 hours. MODERATE conditions. Tango, Sierra, Zulu'),
 d('AIRMET Tango', 'moderate turbulence, sustained surface winds of 30 knots or more, and non-convective LOW-LEVEL WIND SHEAR'),
 d('AIRMET Sierra', 'IFR conditions and/or extensive mountain obscuration'),
 d('AIRMET Zulu', 'moderate icing, and the freezing level heights'),
 d('SIGMET (WS)', 'up to 4 hours. SEVERE and NON-convective: severe icing, severe or extreme turbulence and CAT not associated with thunderstorms, and dust or sandstorms below 3 SM. Hazardous to ALL aircraft'),
 d('Convective SIGMET (WST)', 'issued at 55 past the hour, valid 2 hours. Surface winds 50 knots or more, hail 3/4 inch or larger, tornadoes, or embedded thunderstorms of any intensity'),
 d('What a WST implies', 'severe or greater turbulence, severe icing and low-level wind shear — automatically, without having to say so'),
 d('Surface analysis chart', 'pressure systems, isobars, fronts and air-mass boundaries. Every 3 hours'),
 d('Radar summary chart', 'precipitation type, intensity, coverage, movement and echo tops. Hourly. It shows PRECIPITATION, never cloud'),
 d('Low-level significant weather', 'surface to FL240: IFR, MVFR and VFR areas, turbulence and freezing levels. Four times a day at 0000, 0600, 1200 and 1800Z'),
 d('Convective outlook (AC)', 'a 3-day severe-weather forecast: marginal, slight, enhanced, moderate, high'),
 d('METAR', 'an OBSERVATION, hourly. A SPECI is an unscheduled one issued when something changes significantly'),
 d('TAF', 'a FORECAST, for a 5 SM radius around the station. Four times a day, covering 24 or 30 hours'),
 d('ATIS, AWOS and ASOS', 'ATIS updates hourly, normally at 55 past, with specials as needed. AWOS and ASOS update every minute'),
        ])

WXCODE = ("OralWxCodes", "Winds Aloft & The Standards", "Decoding",
          "Six digits and three standard numbers. Every performance and altimetry question downstream starts from these.",
        [
 d('The format', 'direction relative to TRUE north, speed in knots, temperature in Celsius'),
 d('Nothing close to the ground', 'no wind forecast within 1,500 feet of the station elevation, and no temperature within 2,500 feet of it'),
 d('9900', 'light and variable — less than 5 knots'),
 d('Speeds 100 to 199', '50 is ADDED to the direction and 100 SUBTRACTED from the speed. 731960 is 230 degrees at 119 knots, minus 60 Celsius'),
 d('Speeds 200 or more', 'coded as 99. 7799 is 270 degrees at 199 knots or more'),
 d('Above 24,000 feet', 'the minus sign is dropped, because up there the temperature is always negative'),
 d('Standard sea level', '15 degrees Celsius and 29.92 inches of mercury'),
 d('Standard lapse rate', '2 degrees Celsius and about 1 inch of mercury per 1,000 feet'),
 d('Low pressure', 'in, up and counterclockwise. High pressure is out, down and clockwise — in the northern hemisphere'),
 d('High to low, look out below', 'flying from HIGH pressure to LOW, or from WARM air to COLD, without updating the setting leaves the altimeter reading HIGH — so you are lower than it says. The mnemonic belongs to the cold, low-pressure case'),
 d('Temperature and dew point within 5 degrees', 'expect visible moisture — cloud, dew or fog — and ideal conditions for carburettor icing'),
        ])

# ===================================================================
# I.D & I.E — CROSS-COUNTRY AND AIRSPACE
# ===================================================================

SUA = ("OralSUA", "Special Use Airspace", "Task I.E",
       "Six kinds, and the only two you cannot simply fly through are the two with a letter and a number on the chart. Know which need permission and who grants it.",
        [
 d('Prohibited', 'charted P and a number. You may not enter, full stop. P-49 is Camp David'),
 d('Restricted', 'charted R and a number. Entry requires authorisation from the using or controlling agency. R-4401'),
 d('Warning', 'from 3 NM outward from the coast. The same hazards as a restricted area, but outside sole US jurisdiction — which is why it cannot be "restricted"'),
 d('Alert', 'charted A and a number. High volume of pilot training or unusual aerial activity. No permission needed; extra vigilance is'),
 d('MOA', 'separates military training from IFR traffic. VFR may enter without permission — but ask the controlling agency whether it is hot, and it is on the chart panel'),
 d('TRSA', 'Terminal Radar Service Area. Radar sequencing and separation for VFR, and participation is VOLUNTARY. That is the whole difference from Class C'),
 d('National Security Area', 'a REQUEST to avoid, which a NOTAM can make mandatory'),
 d('TFR', 'a temporary restriction for a hazard, an event, a VIP or a general warning. Carried by FDC NOTAM. Check it before every flight — and before the checkride'),
        ])

SQUAWK = ("OralSquawk", "Codes, Fuel & Right of Way", "The Numbers",
          "The short-answer block. An examiner fires these off quickly, and hesitating on one costs you more credibility than the answer is worth.",
        [
 d('1200', 'VFR'),
 d('7500', 'hijack. Seven five, taken alive'),
 d('7600', 'radio failure. Seven six, working on a fix'),
 d('7700', 'emergency. Seven seven, going to heaven'),
 d('Head-on', 'both aircraft alter course to the RIGHT. 91.113(e)'),
 d('Converging, not head-on', 'the aircraft on the RIGHT has the right of way'),
 d('Overtaking', 'the aircraft being overtaken has the right of way, and you pass on ITS right. 91.113(f) — which is also why clearing turns start to the left'),
 d('Landing', 'the aircraft on final approach, or the lower of two, has the right of way — and you may NOT use that to cut in front of another aircraft on final'),
 d('The pecking order', 'balloon, glider, airship, then airplane or rotorcraft. An aircraft in distress beats everything'),
 d('Fuel by day', '91.151 — to the first point of intended landing plus 30 minutes at NORMAL CRUISING speed'),
 d('Fuel by night', 'plus 45 minutes. WIFA requires 1 HOUR — a school rule stricter than the FAR, and if asked, say both'),
 d('Speed below 10,000 MSL', '250 knots. Beneath a Class B shelf or in a VFR corridor it drops to 200, and within 4 NM of a Class C or D primary airport at or below 2,500 AGL it is also 200'),
        ])

NAVAID = ("OralNavaids", "Navigation Aids", "VOR, DME, GPS",
          "You will not fly the checkride on the VOR, but you will be asked how you would check one and what a radial actually is.",
        [
 d('VOR', 'a VHF station projecting 360 radials. A RADIAL is a line of magnetic bearing, and it always runs FROM the station'),
 d('VOT check', 'plus or minus 4 degrees. The needle centres with a 0 FROM or a 180 TO'),
 d('Ground checkpoint', 'plus or minus 4 degrees. Airborne checkpoint, plus or minus 6'),
 d('Dual VOR cross-check', 'the two receivers must agree within 4 degrees of each other'),
 d('How often', 'every 30 days — but only for IFR. Knowing that it does NOT bind your VFR flight is the point of the question'),
 d('DME', 'distance measuring equipment, and it reads SLANT range. Directly overhead the station it reads your altitude, not zero'),
 d('GPS', 'satellite navigation. Four satellites give a 3-D fix; a fifth allows RAIM, the integrity check that tells you the fix can be trusted'),
 d('WAAS', 'a ground and satellite correction system that tightens GPS accuracy to a few metres — enough for LPV approaches down to 200-foot minimums'),
 d('VFR cruising altitudes', 'more than 3,000 feet AGL: magnetic COURSE 0 to 179 flies odd thousands plus 500; 180 to 359 flies even thousands plus 500'),
 d('Choosing an altitude', 'terrain and obstacle clearance, gliding distance to a landable field, the hemispheric rule, the wind, and staying clear of or under the airspace'),
        ])

# ===================================================================
# I.F — PERFORMANCE
# ===================================================================

ALTS = ("OralAltitudes", "The Five Altitudes", "Task I.F",
        "Name them in order and say which instrument setting produces each. Pressure altitude is the one every performance chart actually wants.",
        [
 d('Indicated', 'what the dial reads with the local setting in the window. QNH'),
 d('Pressure', 'height above the 29.92 datum. Set 29.92 to read it directly. QNE — and it is the input to every performance chart'),
 d('Density', 'pressure altitude corrected for non-standard TEMPERATURE. What the aeroplane actually feels, and what governs its performance'),
 d('True', 'the actual height above mean sea level'),
 d('Absolute', 'height above the ground beneath you. QFE'),
 d('The rule of thumb', '1,000 feet per inch of mercury. A setting BELOW 29.92 puts pressure altitude ABOVE field elevation'),
 d('What raises density altitude', 'high altitude, high temperature, high humidity — and humid air being LESS dense is the half that catches people, because damp air feels heavy'),
 d('What it affects', 'lift from the wing, power from the engine, thrust from the propeller, and drag. All four at once, all in the wrong direction'),
        ])

SPDS = ("OralSpeeds", "The Six Airspeeds", "IAS to Groundspeed",
        "Each one is the one before it plus a correction. Recite the chain and the definitions come out on their own.",
        [
 d('IAS', 'indicated airspeed — what the airspeed indicator reads'),
 d('CAS', 'IAS corrected for instrument and position error. The POH has the table'),
 d('EAS', 'CAS corrected for compressibility. It only starts to matter fast and high, so in a 172 it is a definition, not a number'),
 d('TAS', 'actual speed through the air — EAS corrected for non-standard pressure and temperature'),
 d('Mach number', 'TAS as a ratio of the local speed of sound'),
 d('Groundspeed', 'TAS corrected for wind'),
 d('The chain', 'Indicated, Calibrated, Equivalent, True, Ground. Each step adds one correction, and every correction is a POH or E6B lookup'),
 d('Hot day', 'thinner air means a higher TAS for the same IAS — so the groundspeed is higher and you touch down faster over the ground on the same indicated approach speed'),
        ])

# ===================================================================
# I.G — SYSTEMS
# ===================================================================

ENG = ("OralEngine", "Your Engine", "Task I.G",
       "Six words describe the engine and the examiner expects all six. Then carburettor, mixture and the two abnormal combustion events.",
        [
 d('The engine, in six words', 'Lycoming, four-cylinder, horizontally opposed, air-cooled, normally aspirated, direct drive'),
 d('The four strokes', 'Intake, Compression, Power, Exhaust'),
 d('Carburettor', 'mixes fuel with air and meters it to the cylinders'),
 d('Mixture control', 'sets the amount of FUEL in the fuel-air ratio. You lean as you climb because the air thins and the mixture would otherwise run rich'),
 d('Carburettor heat', 'sends warm air to the carburettor. Warm air is less dense, so the mixture goes RICHER and the RPM drops'),
 d('Why carb ice forms', 'fuel vaporising plus the pressure drop through the venturi can cool the carburettor 60 to 70 degrees F below ambient'),
 d('Favourable conditions', 'below 70 F (21 C) with relative humidity above 80 percent — though it is physically possible up to about 100 F. Your guide’s 38 C at 50 percent is that outer case'),
 d('First indication', 'a loss of RPM with a fixed-pitch propeller. With a constant-speed prop it is a drop in manifold pressure instead'),
 d('When you pull carb heat', 'the RPM drops FIRST — that is the less dense air — then RISES as the ice clears. A rough run while it clears is the ice going through the engine, and it is a good sign'),
 d('Detonation', 'the mixture explodes instead of burning smoothly. Caused by too low a fuel grade, high power with a lean mixture, or reduced cooling in a steep climb or a long ground run'),
 d('Pre-ignition', 'the mixture lights BEFORE the spark, off a hot spot such as a carbon deposit on a plug. The expanding gases push against a piston still coming up on its compression stroke'),
 d('If you suspect either', 'reduce power, lower the nose for cooling, ENRICH the mixture, and open the cowl flaps if fitted'),
        ])

IGN = ("OralIgnition", "Ignition, Fuel & Oil", "The Independent System",
       "The magneto question is the classic one, and its two failure signatures point in opposite directions. Get them the right way round.",
        [
 d('Ignition', 'two engine-driven magnetos, two spark plugs per cylinder, completely INDEPENDENT of the aircraft electrical system. The engine keeps running with the master off'),
 d('Why two', 'redundancy, and a more complete burn from two flame fronts — which is why you lose a little RPM running on one'),
 d('A healthy run-up', 'a small drop on each magneto, within the POH limit, and the two drops roughly equal'),
 d('NO drop on one side', 'that magneto’s P-lead is broken and the engine has been running on the other one all along. Do not fly it'),
 d('Excessive drop', 'fouled plugs or a failing magneto. Leaning briefly at run-up RPM often burns a fouled plug clean'),
 d('The dangerous case', 'a broken P-lead means the switch is not actually grounding that magneto — so the propeller is LIVE even with the switch off. Treat every propeller as live, always'),
 d('Fuel', '100LL, coloured BLUE. 100 is green; jet fuel is clear or straw'),
 d('If your grade is unavailable', 'use the next HIGHER grade, never a lower one. A higher grade takes more pressure before detonating'),
 d('Oil does six things', 'lubricates, cools, seals between piston and cylinder wall, cleans by carrying contaminants to the filter, cushions the moving parts, and protects against corrosion'),
        ])

ELEC = ("OralElectrical", "Electrical & Pitot-Static", "What Runs On What",
        "Split the panel two ways before you answer: what needs electricity, and what needs air. The blockage questions all fall out of that.",
        [
 d('The system', 'an engine-driven alternator, a battery, and a split master switch — ALT and BAT halves'),
 d('What runs on it', 'radios, turn coordinator, fuel gauges, pitot heat, landing, taxi, strobe, position and instrument lights, the flaps (electric in the 172), the stall warning, and the electric fuel pump where fitted'),
 d('Why the alternator reads higher', 'output sits a little above battery voltage so the battery keeps charging'),
 d('Ammeter positive', 'the alternator is charging the battery. NEGATIVE means the battery is carrying the load and the alternator is not — you are on a clock'),
 d('Pitot tube feeds', 'the airspeed indicator, and nothing else'),
 d('Static port feeds', 'the airspeed indicator, the altimeter and the VSI — all three'),
 d('Blocked static', 'the altimeter freezes at the blocked altitude and the VSI sits at zero. The airspeed reads correctly only at that altitude — HIGH below it, LOW above it'),
 d('Alternate static source', 'takes cabin air, which is at a slightly LOWER pressure. So the altimeter reads higher, the airspeed reads faster, and the VSI shows a momentary climb'),
 d('Blocked pitot, drain open', 'the airspeed falls toward zero'),
 d('Blocked pitot AND drain', 'the airspeed behaves like an ALTIMETER — rising in the climb, falling in the descent, with no relation to how fast you are going'),
        ])

GYRO = ("OralGyros", "Gyroscopic Instruments", "Rigidity & Precession",
        "Two principles, three instruments, and one of the three is electric. That last fact is what keeps you upright after a vacuum failure.",
        [
 d('The two principles', 'rigidity in space, and precession'),
 d('Attitude indicator', 'rigidity in space. VACUUM driven. Should be erect and correct within 5 minutes of engine start'),
 d('Heading indicator', 'rigidity in space. VACUUM driven. It cannot find north — you set it against the compass and re-set it roughly every 15 minutes because it drifts'),
 d('Turn coordinator', 'PRECESSION. ELECTRIC — which is exactly why it survives a vacuum failure and becomes your turn reference'),
 d('The ball', 'not a gyro at all. It is an inclinometer, and it shows slip or skid'),
 d('Attitude indicator errors', 'a slight pitch UP on acceleration, a slight pitch DOWN on deceleration, and a small turn error after rolling out from a 180'),
 d('Slip', 'not enough rudder for the bank. The ball falls toward the INSIDE of the turn and the nose points OUTSIDE it. Step on the ball'),
 d('Skid', 'too much rudder for the bank. The ball slides to the OUTSIDE and the nose points INSIDE the turn'),
 d('Why the skid is the killer', 'in a skid the LOWER, inside wing reaches the critical angle first, so it drops and rolls you INTO the turn and toward the ground. That is the base-to-final stall-spin. In a slip the upper wing goes first and the aeroplane rolls toward level'),
        ])

COMPASS = ("OralCompass", "Magnetic Compass Errors", "D V M O N A",
           "Your guide’s mnemonic, and the last two are mirror images of each other. Getting them the wrong way round is the single most common compass error — mind that one.",
        [
 d('D — Deviation', 'magnetic fields inside the aeroplane itself. Corrected on the compass correction card on the panel, and it is specific to that airframe'),
 d('V — Variation', 'the angle between true and magnetic north. East is least, west is best. Shown by isogonic lines on the sectional'),
 d('M — Magnetic dip', 'the card tries to point DOWN toward the magnetic pole. Dip is the physical cause of the next three'),
 d('O — Oscillation', 'the card swings in turbulence. Read the average, do not chase it'),
 d('N — Northerly turning error', 'UNOS — Undershoot North, Overshoot South. Worst on NORTH and SOUTH headings, and absent on east and west'),
 d('A — Acceleration error', 'ANDS — Accelerate North, Decelerate South. Worst on EAST and WEST headings, and absent on north and south'),
 d('The mirror', 'turning error bites on north and south; acceleration error bites on east and west. The mnemonic names the ERROR you see, never the heading you are on'),
 d('When to believe it', 'the compass is only accurate in straight and level unaccelerated flight. That is also when you re-set the heading indicator against it'),
        ])

# ===================================================================
# II — PREFLIGHT PROCEDURES (the WIFA briefings)
# ===================================================================

TAXIBRIEF = ("OralTaxiBrief", "The Taxi Brief (ARCH)", "Task II.B & II.D",
             "PHAK taxi brief, plus the runway-incursion answers. Do this out loud before you release the brakes and the examiner has already scored the Task.",
        [
 d('A — Assigned runway', 'the runway you are planned or cleared for'),
 d('R — Route', 'the taxi route, traced on the diagram before you move'),
 d('C — Crossings', 'crossings and hold-short instructions — and every one of them gets read back'),
 d('H — Hot spots and hazards', 'NOTAMs, closed taxiways or runways, construction, surface conditions'),
 d('Progressive taxi', 'ask for it whenever you are unsure of the instruction or of where you are. It is the fix, not an admission of failure'),
 d('Avoiding an incursion', 'know the hot spots, keep a sterile cockpit, write the instruction down and plot it on the taxi diagram'),
 d('If you get lost', 'stop, hold position, and tell the tower where you think you are'),
 d('Crosswind taxi', 'climb into the wind — aileron INTO the wind when it is ahead of you; dive away from the wind — aileron AWAY and elevator down when it is behind you'),
        ])

TAXICHK = ("OralTaxiCheck", "The Taxi Instrument Check", "What Each One Should Read",
           "A real check, not a glance. Each instrument has a number or a behaviour you are confirming against.",
        [
 d('Airspeed', '0 KIAS'),
 d('Turn coordinator', 'ball centred and wings level when straight. In a turn it shows the turn in the CORRECT direction and the ball swings OPPOSITE'),
 d('Attitude indicator', 'correct pitch and bank within 5 degrees, and erect within 5 minutes of engine start'),
 d('Heading indicator', 'set against the compass, and showing the right headings as you turn'),
 d('Altimeter', 'set to the local altimeter setting, reading field elevation within 75 feet'),
 d('VSI', '0 fpm — and if it is not, note the error and apply it in flight'),
 d('Magnetic compass', 'swinging freely, full of fluid, showing known headings, correction card fitted'),
 d('Nav, comm and GPS', 'set for the departure before you reach the hold short line'),
        ])

PAXBRIEF = ("OralPaxBrief", "The Passenger Brief", "WIFA Version",
            "The WIFA brief, as your school teaches it. 91.107 is the only regulatory part; the rest is what the ACS grades under Flight Deck Management.",
        [
 d('Seat belts', 'how they work and when they must be worn — taxi, takeoff and landing for passengers. This half is 91.107, and it is on YOU to brief it'),
 d('Fire extinguisher', 'where it is and how to use it'),
 d('Air sick bags', 'where they are, before anybody needs one'),
 d('Sterile cockpit', 'no non-essential conversation during taxi, takeoff, landing, or any abnormal'),
 d('Traffic', 'ask them to help look — and to call it by clock position and high or low'),
 d('Emergency exits', 'how the doors open, the evacuation plan, and where to meet afterwards'),
 d('Any questions', 'finish with it out loud. The examiner listens for that line'),
 d('Who briefs', 'the PIC. It cannot be delegated, and doing it in front of the examiner is the cheapest Task on the checkride'),
        ])

# The pre-takeoff brief is ordered, so it is a SEQUENCE: the whole value is
# knowing which case comes at which altitude.
TOBRIEF = ("OralTakeoffBrief", "The Pre-Takeoff Brief", "WIFA — In Order",
           "Your school’s departure emergency brief, in the order you say it. The point is the decision tree: the same failure gets three different answers depending on where you are when it happens.",
        [
 'The triggers ➔ an engine failure, a fire, loss of controllability, a dead airspeed indicator, or any RED annunciation',
 'PRIOR TO ROTATION ➔ throttle to idle, brake straight ahead, and advise the abort on the radio',
 'AFTER ROTATION, enough runway remaining ➔ land straight ahead, stop, announce on the radio',
 'AFTER ROTATION, insufficient runway ➔ pitch for best glide, shallow turns to avoid obstacles, land off the airport',
 'Before that off-airport touchdown ➔ secure fuel and electrical, pop the doors open, announce — so the wings absorb the impact, not the cabin',
 'AFTER ROTATION, at least 1,000 feet ➔ a conservative 180 back to the airport, to any runway, taxiway or open area, announced',
 'Finish ➔ any questions?',
        ])

# ===================================================================
# MCQ — SYSTEMS
# ===================================================================

SYSQ = [
 ("During the run-up you switch from BOTH to RIGHT and there is no RPM drop at all. What does that indicate?",
  ["The LEFT magneto has failed — the engine has been running on the right one alone.",
   "The right magneto is producing more power than normal, which is acceptable.",
   "Both magnetos are healthy; no drop is the ideal result."],
  "Selecting RIGHT cuts the LEFT magneto. If cutting it changes nothing, it was contributing nothing. Two flame fronts always burn a little better than one, so a small drop on each side is the HEALTHY answer and no drop at all is a failure signature. Do not fly it."),
 ("A broken P-lead (magneto grounding wire) has a consequence outside the cockpit. What is it?",
  ["The ignition switch cannot ground that magneto, so the propeller is LIVE even with the switch OFF.",
   "The engine cannot be started until the wire is replaced.",
   "The battery will discharge while the aircraft is parked."],
  "The switch does not power a magneto, it GROUNDS one to stop it. A broken ground means the magneto keeps firing whatever the switch says, so a hand on that propeller can start the engine. This is why you treat every propeller as live and why the answer to a hot mag is a mechanic, not a second try."),
 ("You apply carburettor heat because you suspect ice. What sequence confirms it?",
  ["The RPM drops first, then RISES above where it was — often with a rough run in between.",
   "The RPM rises immediately and keeps rising.",
   "The RPM drops and stays down until the heat is removed."],
  "The initial drop is simply the less dense warm air giving a richer mixture. The RECOVERY above the original RPM is the ice melting, and the roughness in between is the melt water going through the engine. If the RPM drops and just stays there, you had no ice — you only made the mixture rich."),
 ("Conditions are 65 degrees F with relative humidity around 85 percent. What is the carburettor icing risk?",
  ["High — this is squarely inside the band where the FAA says icing is most likely.",
   "None — icing requires an outside air temperature below freezing.",
   "Low — the humidity is high but the temperature is far above freezing."],
  "Below 70 F with relative humidity above 80 percent is the FAA's most-likely band, and this sits inside it. The temperature that matters is inside the carburettor, not outside the aeroplane: vaporisation and the venturi pressure drop can cool it 60 to 70 degrees below ambient. That is how a mild, humid day ices up an engine."),
 ("What is the difference between detonation and pre-ignition?",
  ["Detonation is the mixture exploding instead of burning evenly; pre-ignition is it lighting BEFORE the spark, off a hot spot.",
   "They are two names for the same event.",
   "Detonation happens only at low power; pre-ignition only at high power."],
  "Detonation is about HOW the charge burns — an explosion rather than a controlled front. Pre-ignition is about WHEN it lights — early, from a glowing carbon deposit or a cracked plug, pushing on a piston still rising. Either can destroy an engine, and the response is the same: power back, nose down for cooling, mixture RICH, cowl flaps open."),
 ("Your aircraft calls for 100LL and the field only has a higher grade. What do you do?",
  ["Use the next HIGHER grade — never a lower one.",
   "Use the next lower grade, since a lower grade burns cooler.",
   "Blend the two grades to reach the required octane."],
  "The grade number is how much pressure the fuel takes before it detonates, so going up is conservative and going down invites exactly the failure you are trying to avoid. 100LL is BLUE, 100 is green, and jet fuel is clear or straw — clear fuel going into a piston aeroplane is the one to stop the truck for."),
 ("The static port ices over during a climb. What do the three instruments do?",
  ["The altimeter freezes at the blocked altitude, the VSI reads zero, and the airspeed reads LOW as you climb.",
   "All three read zero.",
   "The altimeter continues to work; only the airspeed and VSI are affected."],
  "All three are static instruments, so all three are affected. With the trapped pressure too HIGH for your new altitude, the pitot-versus-static difference is smaller than it should be and the airspeed under-reads. In a DESCENT the error reverses and the airspeed reads high. Ask which way the trapped value is wrong and the direction follows."),
 ("You open the alternate static source, which draws cabin air. What happens?",
  ["The altimeter reads higher, the airspeed reads faster, and the VSI shows a momentary climb.",
   "The altimeter reads lower, the airspeed reads slower, and the VSI shows a momentary descent.",
   "Nothing changes — cabin pressure equals outside static pressure."],
  "Airflow over the fuselage lowers cabin pressure slightly below true static. A LOWER static reading makes the altimeter think it climbed and makes the airspeed differential bigger, so both read high, and the VSI blips up before settling. The POH gives the correction; the direction is what you must know without it."),
 ("Which instrument keeps working after a complete vacuum failure?",
  ["The turn coordinator — it is electric.",
   "The attitude indicator — it has its own air supply.",
   "None of the gyroscopic instruments."],
  "Attitude indicator and heading indicator are vacuum driven and both die. The turn coordinator is ELECTRIC, which is why it is the one you fly by, along with the compass, the altimeter and the airspeed. Note it also runs on a different principle — precession, while the other two use rigidity in space."),
 ("You are in a turn and the ball has slid to the OUTSIDE of the turn. What is happening and why does it matter?",
  ["A skid — too much rudder for the bank. In a skidded stall the lower inside wing drops and rolls you into the turn.",
   "A slip — not enough rudder for the bank, and the upper wing would stall first.",
   "A coordinated turn; the ball moves outward in any turn."],
  "Ball outside means skid; ball inside means slip. The skid is the dangerous one because the inside, lower wing reaches the critical angle first, so the aeroplane rolls INTO the turn and toward the ground — the classic base-to-final stall-spin from overshooting the turn and adding bottom rudder. In a slip the upper wing goes first and it rolls toward level."),
 ("The ammeter shows a steady discharge in flight. What does that tell you?",
  ["The alternator is not carrying the load — the battery is, and you are on a clock.",
   "The battery is being charged normally after engine start.",
   "The alternator output voltage is too high."],
  "A positive reading is the alternator charging the battery; a negative one is the battery being drained to run the aircraft. Shed what you can, keep what you need to land, and get on the ground before the battery goes. A brief discharge right after start is normal as the battery recovers the cranking energy."),
 ("Why is the ignition system independent of the aircraft electrical system?",
  ["The magnetos are engine-driven and generate their own current, so the engine keeps running with the master OFF.",
   "The magnetos draw from a dedicated backup battery.",
   "It is not — the magnetos are powered by the alternator."],
  "A magneto is a self-contained generator spun by the engine. Total electrical failure costs you radios, lights, flaps and the gauges — it does not cost you the engine. The examiner asks this to see whether you will panic about the engine when the real problem is that you have gone quiet on the radio."),
 ("What does carburettor heat do to the fuel-air mixture, and why?",
  ["It makes it RICHER — warm air is less dense, so the same fuel meets less air.",
   "It makes it LEANER — warm air expands and carries more oxygen.",
   "It has no effect on mixture, only on ice."],
  "Less dense air with unchanged fuel flow is by definition a richer mixture, which is also why the RPM drops when you pull it. On a long descent with carb heat on you may need to lean slightly to keep the engine running smoothly, and that is the answer an examiner is fishing for when they ask what else carb heat changes."),
 ("Which instruments does the PITOT tube feed?",
  ["The airspeed indicator only.",
   "The airspeed indicator and the altimeter.",
   "All three pitot-static instruments."],
  "Pitot feeds one instrument: the airspeed indicator, which compares ram pressure against static. The STATIC port feeds all three — airspeed, altimeter and VSI. Splitting the panel that way before you answer is what makes every blockage question straightforward."),
 ("How does the heading indicator know which way you are pointing?",
  ["It does not — it holds a heading you SET from the compass, and it drifts, so you re-set it periodically.",
   "It senses the earth's magnetic field directly, more accurately than the compass.",
   "It is slaved to the GPS track."],
  "A basic heading indicator is a gyro holding rigidity in space; it measures CHANGE, not direction. Set it against the compass in straight and level unaccelerated flight, and re-set it roughly every 15 minutes because precession and earth rotation walk it off. That is also why the compass, for all its errors, is the master reference."),
 ("What exactly makes an aircraft airworthy?",
  ["It conforms to its type certificate, and it is in condition for safe operation.",
   "It has a current annual inspection and a valid registration.",
   "It has passed all required inspections and the pilot is current."],
  "Two things, and the paperwork is only how you EVIDENCE them. Conformity means it is still the aeroplane the FAA certificated, including AD compliance and any approved alterations. Condition means it is safe today. The pilot's currency has nothing to do with it — merging pilot and aircraft is a category error an examiner will pick up."),
]

# ===================================================================
# MCQ — PREFLIGHT PROCEDURES / GROUND
# ===================================================================

GNDQ = [
 ("You are cleared to taxi via a route that crosses runway 32. What must you do with that instruction?",
  ["Read back the runway crossing instruction in full, and write it down before you move.",
   "Acknowledge with your callsign; a full read-back is only required for takeoff clearances.",
   "Begin taxiing and read it back once you are moving."],
  "Every hold-short and every runway-crossing instruction is a mandatory read-back, and the reason is that the read-back is where a misheard clearance gets caught. Write it down, plot it on the taxi diagram, then move. Sorting out a route while rolling is how an incursion happens."),
 ("You are unsure where you are on the airport after a re-route. What is the correct action?",
  ["Stop, hold position, tell the tower you are unsure of your position, and request a progressive taxi.",
   "Continue at a slow taxi until you recognise a sign or marking.",
   "Return to the ramp without telling anyone and start again."],
  "Stopping is free; guessing is not. Controllers give progressive taxi routinely and it costs you nothing but a moment. The failure mode the examiner is testing for is a pilot who keeps rolling while working it out — the aeroplane is moving toward a runway the whole time they are thinking."),
 ("Taxiing with a quartering TAILWIND from the left, where do the controls go?",
  ["Aileron away from the wind — left aileron down — and the elevator down. Dive away from the wind.",
   "Aileron into the wind and the elevator up. Climb into the wind.",
   "Controls neutral; the correction is only needed with a headwind."],
  "Two rules, and the tailwind case is the one people forget. Climb INTO the wind when it is ahead of you: aileron into it, elevator neutral or up. Dive AWAY from the wind when it is behind you: aileron away, elevator down, which keeps the wind from getting under the tail and the upwind wing. A quartering tailwind is the most hazardous case for a light aeroplane."),
 ("An engine failure at 300 feet AGL, with plenty of runway still ahead. Per the WIFA brief, what do you do?",
  ["Land straight ahead on the remaining runway, stop, and announce it on the radio.",
   "Turn back to the departure runway immediately.",
   "Pitch for best glide and look for a field off the airport."],
  "The brief is a decision tree on altitude and runway remaining. Runway ahead means use it — there is nothing to gain from a turn. The turn back is reserved for AT LEAST 1,000 feet and is described as a conservative 180, not a reflex. The off-airport answer belongs to the case with height but no runway."),
 ("Why does the WIFA brief call for popping the doors before an off-airport landing?",
  ["To stop the airframe jamming them shut on impact, so you can get out.",
   "To reduce cabin pressure and slow the aircraft.",
   "To improve forward visibility over the nose."],
  "A deformed fuselage will trap a closed door and turn a survivable landing into a fatal one. It goes with the rest of the sequence: fuel and electrical secured to reduce fire risk, doors popped, and the touchdown flown so the WINGS absorb the impact rather than the cabin. Brief it out loud before takeoff, every time."),
 ("What does the H in the ARCH taxi brief stand for?",
  ["Hot spots and hazards — NOTAMs, closed runways or taxiways, construction and surface conditions.",
   "Hold short instructions.",
   "Heading, as set on the heading indicator."],
  "Assigned runway, Route, Crossings, Hot spots and hazards. Crossings and hold-shorts are the C, which is why the H has to be something else — it is the airport-specific knowledge you gathered from the chart supplement and the NOTAMs before you started the engine."),
 ("During the taxi check, what should the altimeter read?",
  ["Field elevation within 75 feet, with the local altimeter setting in the window.",
   "Exactly zero, since you are on the ground.",
   "Pressure altitude, with 29.92 set."],
  "91.121 sets the altimeter setting and AIM 7-2-3 gives the 75-foot tolerance against the surveyed field elevation. An altimeter outside that tolerance is a question mark over every altitude you fly that day. Zero belongs to QFE, which is not a US practice, and 29.92 belongs above 18,000."),
 ("During the taxi check you turn left. What should the turn coordinator show?",
  ["The aircraft symbol indicating a LEFT turn, with the ball swinging to the RIGHT.",
   "The aircraft symbol indicating a left turn, with the ball also swinging left.",
   "No indication at all until airborne."],
  "The instrument senses yaw, so it shows the turn correctly on the ground. The BALL is an inclinometer responding to the physical forces of the turn, so it swings to the outside — opposite to the turn. Seeing the ball move with the turn on the ground means something is wrong with the instrument."),
 ("How long after engine start should the attitude indicator be erect and reading correctly?",
  ["Within 5 minutes.",
   "Within 30 seconds.",
   "It only erects once airborne."],
  "Five minutes, and you check it during taxi — correct pitch attitude and wings level within about 5 degrees. A vacuum gyro that is still wandering after that is a gyro or a vacuum problem, and it is far better found on the taxiway than in the first cloud you meet."),
 ("Who is responsible for giving the passenger briefing?",
  ["The pilot in command — it cannot be delegated.",
   "The flight school, before the passenger reaches the aircraft.",
   "Any certificated pilot on board."],
  "91.107 puts briefing the belts on the PIC, and the ACS grades the rest under Flight Deck Management. Practically it is also the easiest credit on the checkride: brief the belts, extinguisher, sick bags, sterile cockpit, traffic spotting, exits and the evacuation plan, and finish by asking for questions."),
 ("What is the 'sterile cockpit' and when does it apply?",
  ["No non-essential conversation during taxi, takeoff, landing or any abnormal situation.",
   "A requirement that the cabin be cleaned before each flight.",
   "A rule that only the pilot may speak on the radio at any time."],
  "It is a discipline borrowed from the airlines and it is briefed to the passengers so they know when to stop talking. The phases it covers are the ones with the highest workload and the least margin — which are also the phases where a runway incursion or a missed radio call happens."),
 ("You are about to taxi onto a runway to depart. The tower says 'line up and wait'. What has it NOT given you?",
  ["A takeoff clearance — line up and wait is never one.",
   "Permission to enter the runway.",
   "Permission to line up on the centreline."],
  "It authorises you onto the runway and nothing more. If a takeoff clearance does not follow within a reasonable time, contact ATC — AIM 5-2-5 sets no fixed number of seconds, but the FAA's own review of these accidents found two minutes or more typically elapsed. Sitting stationary on an active runway is one of the highest-exposure positions in aviation."),
]

# ===================================================================
# ASSEMBLY
# ===================================================================

DEFS2 = [QUAL, PRIV, DOCS, BASICMED,
         INSP, MAINT, POHEQ,
         WXSRC, WXPROD, WXCODE,
         SUA, SQUAWK, NAVAID,
         ALTS, SPDS,
         ENG, IGN, ELEC, GYRO, COMPASS,
         TAXIBRIEF, TAXICHK, PAXBRIEF]

SEQS2 = [TOBRIEF]

BANKS2 = [
    ("OralSystems", "Systems — Scenarios", SYSQ,
     [("How the C172 systems work", "https://www.youtube.com/results?search_query=cessna+172+systems+explained+engine+electrical+fuel+private+pilot"),
      ("Magneto checks and the run-up", "https://www.youtube.com/results?search_query=magneto+check+runup+P-lead+explained+private+pilot"),
      ("Pitot-static system and blockages", "https://www.youtube.com/results?search_query=pitot+static+system+blockage+alternate+static+source+explained"),
      ("Carburettor icing", "https://www.youtube.com/results?search_query=carburetor+icing+carb+heat+explained+private+pilot")]),
    ("OralGround", "Ground Operations — Scenarios", GNDQ,
     [("Taxi briefings and runway incursions", "https://www.youtube.com/results?search_query=runway+incursion+avoidance+taxi+briefing+hot+spots+explained"),
      ("Crosswind taxi control positions", "https://www.youtube.com/results?search_query=crosswind+taxi+control+positions+climb+into+dive+away+explained"),
      ("The departure emergency briefing", "https://www.youtube.com/results?search_query=takeoff+emergency+briefing+engine+failure+after+takeoff+impossible+turn")]),
]

MCQ_DESC2 = {
    'OralSystems': "Task I.G asked the way an examiner asks it — not “what is a magneto” but “it did this on the run-up, now what”. Every item here has a failure signature attached to it.",
    'OralGround': "Area II: flight deck management, the taxi brief, the passenger brief and the departure emergency brief, including the WIFA decision tree. These Tasks are graded while you are simply operating the aeroplane, which is what makes them cheap to pass and easy to forget.",
}

# Sub-sections, in ACS order. The guide's own table of contents.
SPEC2 = [
    ("The Checkride",                  ["OralACS", "OralAreas", "OralBring", "OralOutcome"]),
    ("I.A — Pilot Qualifications",     ["OralQual", "OralPrivileges", "OralDocs", "OralBasicMed", "OralPrereq"]),
    ("I.B — Airworthiness",            ["OralInspections", "OralMaint", "OralPOH", "OralInop"]),
    ("I.C — Weather",                  ["OralWxSources", "OralWxProducts", "OralWxCodes"]),
    ("I.D & I.E — Cross-Country & Airspace", ["OralSUA", "OralSquawk", "OralNavaids", "OralXC"]),
    ("I.F — Performance",              ["OralAltitudes", "OralSpeeds"]),
    ("I.G — Systems",                  ["OralEngine", "OralIgnition", "OralElectrical", "OralGyros", "OralCompass", "OralSystems"]),
    ("I.H — Human Factors",            ["OralHypoxia", "OralIllusions", "OralAttitudes", "OralAeromed"]),
    ("II — Preflight Procedures",      ["OralTaxiBrief", "OralTaxiCheck", "OralPaxBrief", "OralTakeoffBrief", "OralGround"]),
]
