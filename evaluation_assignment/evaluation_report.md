# Evaluation Report — Golden Set

Golden set size: 40 queries, k=5

## Retrieval Accuracy (Hit@k, did the correct document appear in the top-k results)

| Mode | Accuracy |
| --- | --- |
| hybrid | 98% |

## Faithfulness (answers generated with `hybrid` retrieval)

| Metric | Value |
| --- | --- |
| cited_expected_document_rate | 95% |
| judged_count | 40 |
| pending_manual_judgment | 0 |
| graph_expansion_items | 10 |
| graph_expansion_hit_rate | 90% |
| faithful_rate | 90% |
| partially_faithful_rate | 2% |
| unfaithful_rate | 8% |

## Per-query detail

### gs-01: Does racial segregation in public schools violate the Equal Protection Clause even if the physical facilities are equal?
- Expected document: [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) (p. 6, sha256 7021074961cf…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the ground truth holding with direct quotes, no unsupported additions.

**Expected answer:** Yes. In Brown v. Board of Education, the Supreme Court held that segregating white and Black children in public schools solely on the basis of race, even where physical facilities and other tangible factors are equal, denies Black children the equal protection of the laws guaranteed by the Fourteenth Amendment.

**Generated answer:** Yes, racial segregation in public schools violates the Equal Protection Clause even if the physical facilities are equal. The Supreme Court concluded that "segregation of children in public schools solely on the basis of race, pursuant to state laws permitting or requiring such segregation, denies to Negro children the equal protection of the laws guaranteed by the Fourteenth Amendment, even though the physical facilities and other 'tangible' factors of white and Negro schools may be equal" [SOURCE 4]. Additionally, the Court stated that "the doctrine of 'separate but equal' has no place" in public education, affirming that "separate educational facilities are inherently unequal" [SOURCE 2].

**Sources provided to the model:**

1. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 6, sha256 7021074961cf… (expected)
2. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 13, sha256 7021074961cf… (expected)
3. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 11, sha256 7021074961cf… (expected)
4. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 1, sha256 7021074961cf… (expected)
5. [Equal Protection](https://www.law.cornell.edu/wex/equal_protection) — p. 1, sha256 4526d62b142c…
6. [Plessy v. Ferguson](https://tile.loc.gov/storage-services/service/ll/usrep/usrep163/usrep163537/usrep163537.pdf) — p. 8, sha256 1bd8154d5ed6…

### gs-02: What must police do before using statements from a custodial interrogation at trial, according to Miranda v. Arizona?
- Expected document: [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) (p. 1, sha256 31e7666853b8…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches Miranda warning requirements; extra detail on cessation/waiver is accurate to the case.

**Expected answer:** Before interrogating a person in custody, police must clearly inform them that they have the right to remain silent, that anything they say can be used against them in court, that they have the right to consult a lawyer and have the lawyer present during interrogation, and that a lawyer will be appointed for them if they cannot afford one. Statements obtained without these warnings cannot be used by the prosecution.

**Generated answer:** Before using statements from a custodial interrogation at trial, police must take certain procedural safeguards to ensure that the defendant's Fifth Amendment privilege against self-incrimination is protected. Specifically, the following must be observed:

1. The person in custody must be clearly informed that he has the right to remain silent and that anything he says can be used against him in court.
2. He must be informed that he has the right to consult with a lawyer and to have the lawyer present during interrogation. If he is indigent, a lawyer will be appointed to represent him.
3. If the individual indicates that he wishes to remain silent, the interrogation must cease. If he indicates that he wants an attorney, the questioning must also cease until an attorney is present.
4. In cases where a statement is taken without the presence of an attorney, the government has the burden to demonstrate that the defendant knowingly and intelligently waived his right to counsel.
5. Answering some questions during interrogation does not constitute a waiver of the right to remain silent thereafter; he may invoke this right at any time [SOURCE 5].

**Sources provided to the model:**

1. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 1, sha256 31e7666853b8… (expected)
2. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 10, sha256 31e7666853b8… (expected)
3. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 6, sha256 31e7666853b8… (expected)
4. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 14, sha256 31e7666853b8… (expected)
5. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 2, sha256 31e7666853b8… (expected)
6. [Gideon v. Wainwright](https://tile.loc.gov/storage-services/service/ll/usrep/usrep372/usrep372335/usrep372335.pdf) — p. 17, sha256 2d3219523cb2…
7. [Mapp v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep367/usrep367643/usrep367643.pdf) — p. 42, sha256 c6770815d86f…

### gs-03: What did the Supreme Court hold about the scope of the Second Amendment in District of Columbia v. Heller?
- Expected document: [District of Columbia v. Heller](https://tile.loc.gov/storage-services/service/ll/usrep/usrep554/usrep554570/usrep554570.pdf) (p. 1, sha256 8ea329fdac74…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — States the core Second Amendment holding correctly with accurate supporting detail.

**Expected answer:** The Court held that the Second Amendment protects an individual's right to possess a firearm unconnected with service in a militia, and to use that firearm for traditionally lawful purposes such as self-defense within the home.

**Generated answer:** The Supreme Court held that the Second Amendment protects an individual right to possess a firearm unconnected with service in a militia and to use that arm for traditionally lawful purposes, such as self-defense within the home [SOURCE 1]. The Court emphasized that the Second Amendment right is not unlimited and does not imply a right to keep and carry any weapon in any manner for any purpose. However, it specifically ruled that the District of Columbia's total ban on handgun possession in the home violated the Second Amendment, as did the requirement that firearms in the home be kept nonfunctional [SOURCE 2]. Thus, the Court concluded that the District must permit individuals to register handguns and issue licenses for them, assuming they are not disqualified from exercising Second Amendment rights [SOURCE 3].

**Sources provided to the model:**

1. [District of Columbia v. Heller](https://tile.loc.gov/storage-services/service/ll/usrep/usrep554/usrep554570/usrep554570.pdf) — p. 1, sha256 8ea329fdac74… (expected)
2. [District of Columbia v. Heller](https://tile.loc.gov/storage-services/service/ll/usrep/usrep554/usrep554570/usrep554570.pdf) — p. 2, sha256 8ea329fdac74… (expected)
3. [District of Columbia v. Heller](https://tile.loc.gov/storage-services/service/ll/usrep/usrep554/usrep554570/usrep554570.pdf) — p. 3, sha256 8ea329fdac74… (expected)
4. [District of Columbia v. Heller](https://tile.loc.gov/storage-services/service/ll/usrep/usrep554/usrep554570/usrep554570.pdf) — p. 5, sha256 8ea329fdac74… (expected)
5. [District of Columbia v. Heller](https://tile.loc.gov/storage-services/service/ll/usrep/usrep554/usrep554570/usrep554570.pdf) — p. 7, sha256 8ea329fdac74… (expected)

### gs-04: What did the Supreme Court hold about the EPA's 'plantwide' definition of stationary source in Chevron v. NRDC?
- Expected document: [Chevron U.S.A., Inc. v. Natural Resources Defense Council, Inc.](https://tile.loc.gov/storage-services/service/ll/usrep/usrep467/usrep467837/usrep467837.pdf) (p. 23, sha256 b71f216d9e95…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **unfaithful** — Never states the Court's actual holding (that the plantwide/bubble definition was permissible); instead presents the respondents' losing argument right after the word 'held,' which could mislead a reader about the outcome.

**Expected answer:** The Court held that the EPA's plantwide (bubble concept) definition of the statutory term 'stationary source' was a permissible construction of the Clean Air Act, since Congress had not directly addressed the precise question at issue and the agency's interpretation was reasonable.

**Generated answer:** The Supreme Court in Chevron U.S.A., Inc. v. Natural Resources Defense Council, Inc. held that the respondents contended the text of the Act requires the EPA to use a dual definition of "stationary source," meaning that if either a component of a plant or the plant as a whole emits over 100 tons of pollutant, it qualifies as a major stationary source. This interpretation differed from that of the Court of Appeals, which viewed the statutory definition as flexible enough to cover various interpretations, including a plantwide definition. The Court noted that the dispute centered around the applicability of definitions under the statute concerning programs designed to maintain clean air and improve air quality [SOURCE 2].

**Sources provided to the model:**

1. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 1, sha256 2bd1c27f2a0f…
2. [Chevron U.S.A., Inc. v. Natural Resources Defense Council, Inc.](https://tile.loc.gov/storage-services/service/ll/usrep/usrep467/usrep467837/usrep467837.pdf) — p. 23, sha256 b71f216d9e95… (expected)
3. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 1, sha256 2bd1c27f2a0f…
4. [Chevron U.S.A., Inc. v. Natural Resources Defense Council, Inc.](https://tile.loc.gov/storage-services/service/ll/usrep/usrep467/usrep467837/usrep467837.pdf) — p. 13, sha256 b71f216d9e95… (expected)
5. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 2, sha256 2bd1c27f2a0f…
6. [Korematsu v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep323/usrep323214/usrep323214.pdf) — p. 12, sha256 2fdaef6d2e55…
7. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 2, sha256 7021074961cf…

### gs-05: Did burning the American flag as a form of political protest count as protected expression under the First Amendment in Texas v. Johnson?
- Expected document: [Texas v. Johnson](https://tile.loc.gov/storage-services/service/ll/usrep/usrep491/usrep491397/usrep491397.pdf) (p. 1, sha256 a28c0376c798…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **partially_faithful** — Reaches the correct bottom-line conclusion but attributes the reasoning to the Texas Court of Criminal Appeals without clarifying the U.S. Supreme Court affirmed this as its own holding.

**Expected answer:** Yes. The Court held that Johnson's flag burning was expressive conduct implicating the First Amendment, and that Texas's asserted interest in preventing breaches of the peace was not implicated because the government cannot assume that provocative expression will incite a riot.

**Generated answer:** Yes, burning the American flag as a form of political protest was considered protected expression under the First Amendment in Texas v. Johnson. The court found that Johnson's conduct constituted expressive conduct that was clearly intended to convey a political message during a demonstration. The Texas Court of Criminal Appeals recognized that Johnson's flag burning was symbolic speech protected by the First Amendment, concluding that the State could not criminally sanction him for this act in these circumstances [SOURCE 2], [SOURCE 4].

**Sources provided to the model:**

1. [Texas v. Johnson](https://tile.loc.gov/storage-services/service/ll/usrep/usrep491/usrep491397/usrep491397.pdf) — p. 1, sha256 a28c0376c798… (expected)
2. [Texas v. Johnson](https://tile.loc.gov/storage-services/service/ll/usrep/usrep491/usrep491397/usrep491397.pdf) — p. 1, sha256 a28c0376c798… (expected)
3. [Texas v. Johnson](https://tile.loc.gov/storage-services/service/ll/usrep/usrep491/usrep491397/usrep491397.pdf) — p. 3, sha256 a28c0376c798… (expected)
4. [Texas v. Johnson](https://tile.loc.gov/storage-services/service/ll/usrep/usrep491/usrep491397/usrep491397.pdf) — p. 4, sha256 a28c0376c798… (expected)
5. [Texas v. Johnson](https://tile.loc.gov/storage-services/service/ll/usrep/usrep491/usrep491397/usrep491397.pdf) — p. 6, sha256 a28c0376c798… (expected)

### gs-06: In United States v. Nixon, did the Court treat the dispute between the Special Prosecutor and the President as a non-justiciable 'intra-branch dispute'?
- Expected document: [United States v. Nixon](https://tile.loc.gov/storage-services/service/ll/usrep/usrep418/usrep418683/usrep418683.pdf) (p. 1, sha256 04f87a19ea67…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Accurately restates the justiciability holding and standard.

**Expected answer:** No. The Court held that the mere assertion of an intra-branch dispute, without more, does not defeat federal jurisdiction, and that the dispute between the Special Prosecutor and the President presented a justiciable controversy.

**Generated answer:** No, the Court did not treat the dispute between the Special Prosecutor and the President as a non-justiciable "intra-branch dispute." The District Court rejected the contention that the dispute was nonjusticiable because it was "intra-executive" in character. The court concluded that a justiciable controversy was presented, and that the judiciary had the authority to review the President's assertion of executive privilege [SOURCE 3].

**Sources provided to the model:**

1. [United States v. Nixon](https://tile.loc.gov/storage-services/service/ll/usrep/usrep418/usrep418683/usrep418683.pdf) — p. 1, sha256 04f87a19ea67… (expected)
2. [United States v. Nixon](https://tile.loc.gov/storage-services/service/ll/usrep/usrep418/usrep418683/usrep418683.pdf) — p. 2, sha256 04f87a19ea67… (expected)
3. [United States v. Nixon](https://tile.loc.gov/storage-services/service/ll/usrep/usrep418/usrep418683/usrep418683.pdf) — p. 7, sha256 04f87a19ea67… (expected)
4. [United States v. Nixon](https://tile.loc.gov/storage-services/service/ll/usrep/usrep418/usrep418683/usrep418683.pdf) — p. 2, sha256 04f87a19ea67… (expected)
5. [United States v. Nixon](https://tile.loc.gov/storage-services/service/ll/usrep/usrep418/usrep418683/usrep418683.pdf) — p. 5, sha256 04f87a19ea67… (expected)

### gs-07: What Code does the Tax Cuts and Jobs Act (Pub. L. 115-97) refer to when it amends 'the Code'?
- Expected document: [Tax Cuts and Jobs Act](https://www.govinfo.gov/content/pkg/PLAW-115publ97/pdf/PLAW-115publ97.pdf) (p. 2, sha256 4f9ad9b1029a…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Directly and correctly identifies the Internal Revenue Code of 1986.

**Expected answer:** Except as otherwise expressly provided, the Tax Cuts and Jobs Act states that any amendment or repeal expressed in terms of an amendment to, or repeal of, a section or provision is a reference to a section or provision of the Internal Revenue Code of 1986.

**Generated answer:** The Tax Cuts and Jobs Act (Pub. L. 115-97) refers to the Internal Revenue Code of 1986 when it amends 'the Code' [SOURCE 1].

**Sources provided to the model:**

1. [Tax Cuts and Jobs Act](https://www.govinfo.gov/content/pkg/PLAW-115publ97/pdf/PLAW-115publ97.pdf) — p. 2, sha256 4f9ad9b1029a… (expected)
2. [Tax Cuts and Jobs Act](https://www.govinfo.gov/content/pkg/PLAW-115publ97/pdf/PLAW-115publ97.pdf) — p. 19, sha256 4f9ad9b1029a… (expected)
3. [Tax Cuts and Jobs Act](https://www.govinfo.gov/content/pkg/PLAW-115publ97/pdf/PLAW-115publ97.pdf) — p. 18, sha256 4f9ad9b1029a… (expected)
4. [Tax Cuts and Jobs Act](https://www.govinfo.gov/content/pkg/PLAW-115publ97/pdf/PLAW-115publ97.pdf) — p. 7, sha256 4f9ad9b1029a… (expected)
5. [Tax Cuts and Jobs Act](https://www.govinfo.gov/content/pkg/PLAW-115publ97/pdf/PLAW-115publ97.pdf) — p. 42, sha256 4f9ad9b1029a… (expected)

### gs-08: What is the stated purpose of the Dodd-Frank Wall Street Reform and Consumer Protection Act?
- Expected document: [Dodd-Frank Wall Street Reform and Consumer Protection Act](https://www.govinfo.gov/content/pkg/PLAW-111publ203/pdf/PLAW-111publ203.pdf) (p. 2, sha256 8460069ded90…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the stated purpose of Dodd-Frank verbatim.

**Expected answer:** Dodd-Frank was enacted to promote the financial stability of the United States by improving accountability and transparency in the financial system, to end 'too big to fail,' to protect the American taxpayer by ending bailouts, and to protect consumers from abusive financial services practices.

**Generated answer:** The stated purpose of the Dodd-Frank Wall Street Reform and Consumer Protection Act is "to promote the financial stability of the United States by improving accountability and transparency in the financial system, to end 'too big to fail', to protect the American taxpayer by ending bailouts, to protect consumers from abusive financial services practices, and for other purposes" [SOURCE 1].

**Sources provided to the model:**

1. [Dodd-Frank Wall Street Reform and Consumer Protection Act](https://www.govinfo.gov/content/pkg/PLAW-111publ203/pdf/PLAW-111publ203.pdf) — p. 2, sha256 8460069ded90… (expected)
2. [Dodd-Frank Wall Street Reform and Consumer Protection Act](https://www.govinfo.gov/content/pkg/PLAW-111publ203/pdf/PLAW-111publ203.pdf) — p. 1, sha256 8460069ded90… (expected)
3. [Dodd-Frank Wall Street Reform and Consumer Protection Act](https://www.govinfo.gov/content/pkg/PLAW-111publ203/pdf/PLAW-111publ203.pdf) — p. 10, sha256 8460069ded90… (expected)
4. [Dodd-Frank Wall Street Reform and Consumer Protection Act](https://www.govinfo.gov/content/pkg/PLAW-111publ203/pdf/PLAW-111publ203.pdf) — p. 21, sha256 8460069ded90… (expected)
5. [Dodd-Frank Wall Street Reform and Consumer Protection Act](https://www.govinfo.gov/content/pkg/PLAW-111publ203/pdf/PLAW-111publ203.pdf) — p. 9, sha256 8460069ded90… (expected)

### gs-09: What was the stated purpose of the USA PATRIOT Act of 2001?
- Expected document: [USA PATRIOT Act](https://www.govinfo.gov/content/pkg/PLAW-107publ56/pdf/PLAW-107publ56.pdf) (p. 2, sha256 bed9884cea6a…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the stated purpose of the USA PATRIOT Act.

**Expected answer:** The USA PATRIOT Act was enacted to deter and punish terrorist acts in the United States and around the world, and to enhance law enforcement investigatory tools.

**Generated answer:** The stated purpose of the USA PATRIOT Act of 2001 was to deter and punish terrorist acts in the United States and around the world, enhance law enforcement investigatory tools, and for other purposes [SOURCE 1].

**Sources provided to the model:**

1. [USA PATRIOT Act](https://www.govinfo.gov/content/pkg/PLAW-107publ56/pdf/PLAW-107publ56.pdf) — p. 2, sha256 bed9884cea6a… (expected)
2. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 1, sha256 2bd1c27f2a0f…
3. [USA PATRIOT Act](https://www.govinfo.gov/content/pkg/PLAW-107publ56/pdf/PLAW-107publ56.pdf) — p. 1, sha256 bed9884cea6a… (expected)
4. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 1, sha256 2bd1c27f2a0f…
5. [USA PATRIOT Act](https://www.govinfo.gov/content/pkg/PLAW-107publ56/pdf/PLAW-107publ56.pdf) — p. 7, sha256 bed9884cea6a… (expected)
6. [Korematsu v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep323/usrep323214/usrep323214.pdf) — p. 4, sha256 2fdaef6d2e55…
7. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 2, sha256 7021074961cf…

### gs-10: What is the Sarbanes-Oxley Act of 2002 intended to protect, and how?
- Expected document: [Sarbanes-Oxley Act of 2002](https://www.govinfo.gov/content/pkg/PLAW-107publ204/pdf/PLAW-107publ204.pdf) (p. 1, sha256 f6666256313b…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the stated purpose; added mechanism description is general and accurate.

**Expected answer:** The Sarbanes-Oxley Act was enacted to protect investors by improving the accuracy and reliability of corporate disclosures made pursuant to the securities laws.

**Generated answer:** The Sarbanes-Oxley Act of 2002 is intended to protect investors by improving the accuracy and reliability of corporate disclosures made pursuant to the securities laws [SOURCE 1]. It accomplishes this through various provisions that establish regulatory standards, enhance corporate responsibility, and enforce penalties for fraud within publicly traded companies [SOURCE 2][SOURCE 4]. By mandating stronger internal controls and requiring accountability from corporate executives, the Act aims to foster transparency and integrity in financial reporting [SOURCE 3][SOURCE 5].

**Sources provided to the model:**

1. [Sarbanes-Oxley Act of 2002](https://www.govinfo.gov/content/pkg/PLAW-107publ204/pdf/PLAW-107publ204.pdf) — p. 1, sha256 f6666256313b… (expected)
2. [Sarbanes-Oxley Act of 2002](https://www.govinfo.gov/content/pkg/PLAW-107publ204/pdf/PLAW-107publ204.pdf) — p. 2, sha256 f6666256313b… (expected)
3. [Sarbanes-Oxley Act of 2002](https://www.govinfo.gov/content/pkg/PLAW-107publ204/pdf/PLAW-107publ204.pdf) — p. 5, sha256 f6666256313b… (expected)
4. [Sarbanes-Oxley Act of 2002](https://www.govinfo.gov/content/pkg/PLAW-107publ204/pdf/PLAW-107publ204.pdf) — p. 2, sha256 f6666256313b… (expected)
5. [Sarbanes-Oxley Act of 2002](https://www.govinfo.gov/content/pkg/PLAW-107publ204/pdf/PLAW-107publ204.pdf) — p. 22, sha256 f6666256313b… (expected)

### gs-11: What did HIPAA (the Health Insurance Portability and Accountability Act of 1996) amend, and what were its goals?
- Expected document: [Health Insurance Portability and Accountability Act of 1996](https://www.govinfo.gov/content/pkg/PLAW-104publ191/pdf/PLAW-104publ191.pdf) (p. 2, sha256 377ed1f8520e…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches HIPAA's amendment target and goals nearly verbatim.

**Expected answer:** HIPAA amended the Internal Revenue Code of 1986 to improve the portability and continuity of health insurance coverage in the group and individual markets, to combat waste, fraud, and abuse in health insurance and health care delivery, to promote the use of medical savings accounts, to improve access to long-term care services, and to simplify the administration of health insurance.

**Generated answer:** The Health Insurance Portability and Accountability Act of 1996 (HIPAA) amended the Internal Revenue Code of 1986. Its goals were to improve portability and continuity of health insurance coverage in the group and individual markets, combat waste, fraud, and abuse in health insurance and health care delivery, promote the use of medical savings accounts, improve access to long-term care services and coverage, and simplify the administration of health insurance, among other purposes [SOURCE 1].

**Sources provided to the model:**

1. [Health Insurance Portability and Accountability Act of 1996](https://www.govinfo.gov/content/pkg/PLAW-104publ191/pdf/PLAW-104publ191.pdf) — p. 2, sha256 377ed1f8520e… (expected)
2. [Health Insurance Portability and Accountability Act of 1996](https://www.govinfo.gov/content/pkg/PLAW-104publ191/pdf/PLAW-104publ191.pdf) — p. 1, sha256 377ed1f8520e… (expected)
3. [Health Insurance Portability and Accountability Act of 1996](https://www.govinfo.gov/content/pkg/PLAW-104publ191/pdf/PLAW-104publ191.pdf) — p. 3, sha256 377ed1f8520e… (expected)
4. [Patient Protection and Affordable Care Act](https://www.govinfo.gov/content/pkg/PLAW-111publ148/pdf/PLAW-111publ148.pdf) — p. 1, sha256 f5112f582ef4…
5. [Health Insurance Portability and Accountability Act of 1996](https://www.govinfo.gov/content/pkg/PLAW-104publ191/pdf/PLAW-104publ191.pdf) — p. 2, sha256 377ed1f8520e… (expected)

### gs-12: What does the Fourth Amendment protect against, according to the Wex commentary?
- Expected document: [Fourth Amendment](https://www.law.cornell.edu/wex/fourth_amendment) (p. 1, sha256 6246bf76e71e…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the Fourth Amendment commentary with no unsupported claims.

**Expected answer:** The Fourth Amendment protects the right of people to be secure in their persons, houses, papers, and effects against unreasonable searches and seizures, and requires that warrants be supported by probable cause and particularly describe the place to be searched and the persons or things to be seized. Its ultimate goal is to protect privacy and freedom from unreasonable government intrusion, though it only protects against unreasonable searches and seizures done by the government.

**Generated answer:** According to the Wex commentary, the Fourth Amendment protects against "unreasonable searches and seizures" by the government, ensuring the right of the people to be secure in their persons, houses, papers, and effects. The ultimate goal of this provision is to protect people's right to privacy and freedom from unreasonable intrusions by the government [SOURCE 1].

**Sources provided to the model:**

1. [Fourth Amendment](https://www.law.cornell.edu/wex/fourth_amendment) — p. 1, sha256 6246bf76e71e… (expected)
2. [Fourth Amendment](https://www.law.cornell.edu/wex/fourth_amendment) — p. 1, sha256 6246bf76e71e… (expected)
3. [Terry v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep392/usrep392001/usrep392001.pdf) — p. 12, sha256 dda7b8f8fb26…
4. [Fourth Amendment](https://www.law.cornell.edu/wex/fourth_amendment) — p. 1, sha256 6246bf76e71e… (expected)
5. [Mapp v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep367/usrep367643/usrep367643.pdf) — p. 13, sha256 c6770815d86f…

### gs-13: What rights does the First Amendment protect, according to the Wex commentary?
- Expected document: [First Amendment](https://www.law.cornell.edu/wex/first_amendment) (p. 1, sha256 10c5270eef66…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches and appropriately elaborates on First Amendment protections.

**Expected answer:** The First Amendment protects freedom of religion and freedom of expression from government interference. It prohibits laws establishing a national religion, impeding the free exercise of religion, abridging freedom of speech, infringing the freedom of the press, interfering with the right to peaceably assemble, or prohibiting people from petitioning the government for redress of grievances.

**Generated answer:** The First Amendment protects the following rights:

1. Freedom of religion: It prohibits the government from establishing a national religion and protects the free exercise of religion by individuals [SOURCE 1].

2. Freedom of speech: It allows individuals to express themselves without government interference or regulation [SOURCE 3].

3. Freedom of the press: This right is part of the broader protection of freedom of expression and allows individuals to publish and disseminate information [SOURCE 5].

4. Right to peaceably assemble: This right enables individuals to gather for lawful purposes, which includes the implicit right to association and belief [SOURCE 5].

5. Right to petition the government: Individuals have the right to petition the government for a redress of grievances [SOURCE 1]. 

Overall, the First Amendment guards against government interference in these fundamental rights [SOURCE 1].

**Sources provided to the model:**

1. [First Amendment](https://www.law.cornell.edu/wex/first_amendment) — p. 1, sha256 10c5270eef66… (expected)
2. [District of Columbia v. Heller](https://tile.loc.gov/storage-services/service/ll/usrep/usrep554/usrep554570/usrep554570.pdf) — p. 96, sha256 8ea329fdac74…
3. [First Amendment](https://www.law.cornell.edu/wex/first_amendment) — p. 1, sha256 10c5270eef66… (expected)
4. [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) — p. 132, sha256 47426f1f570e…
5. [First Amendment](https://www.law.cornell.edu/wex/first_amendment) — p. 1, sha256 10c5270eef66… (expected)
6. [New York Times Co. v. Sullivan](https://tile.loc.gov/storage-services/service/ll/usrep/usrep376/usrep376254/usrep376254.pdf) — p. 32, sha256 cf04431df4b6…
7. [Schenck v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep249/usrep249047/usrep249047.pdf) — p. 5, sha256 2e26f45f598e…

### gs-14: What is the constitutional source of the 'due process' requirement, and to whom does it apply?
- Expected document: [Due Process](https://www.law.cornell.edu/wex/due_process) (p. 1, sha256 5e8f57b6f5f1…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the Due Process Clause explanation and its constitutional sourcing.

**Expected answer:** Due process derives from the Fifth Amendment, which provides that no one shall be deprived of life, liberty, or property without due process of law by the federal government. The Fourteenth Amendment, ratified in 1868, uses the same words in its Due Process Clause to extend this obligation to the states.

**Generated answer:** The constitutional source of the 'due process' requirement is primarily found in the Fifth Amendment of the U.S. Constitution, which states that no one shall be "deprived of life, liberty or property without due process of law" by the federal government. Additionally, the Fourteenth Amendment, ratified in 1868, reiterates this principle with the same eleven words in its Due Process Clause, extending this obligation to the states. Thus, it applies to both the federal government and state governments [SOURCE 1].

**Sources provided to the model:**

1. [Due Process](https://www.law.cornell.edu/wex/due_process) — p. 1, sha256 5e8f57b6f5f1… (expected)
2. [Due Process](https://www.law.cornell.edu/wex/due_process) — p. 1, sha256 5e8f57b6f5f1… (expected)
3. [Due Process](https://www.law.cornell.edu/wex/due_process) — p. 1, sha256 5e8f57b6f5f1… (expected)
4. [Due Process](https://www.law.cornell.edu/wex/due_process) — p. 1, sha256 5e8f57b6f5f1… (expected)
5. [Due Process](https://www.law.cornell.edu/wex/due_process) — p. 1, sha256 5e8f57b6f5f1… (expected)

### gs-15: What are the basic elements required for an agreement to be a legally enforceable contract, according to the Wex commentary?
- Expected document: [Contract](https://www.law.cornell.edu/wex/contract) (p. 1, sha256 2053f9af7c4d…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Lists exactly the four contract elements from the reference.

**Expected answer:** The basic elements are mutual assent (offer and acceptance), consideration (something of value exchanged), capacity (such as minimum age and sound mind), and legality (a lawful purpose). In some states, a valid substitute can satisfy the consideration element.

**Generated answer:** The basic elements required for an agreement to be a legally enforceable contract, according to the Wex commentary, are:

1. Mutual assent (offer and acceptance)
2. Consideration (something of value is exchanged)
3. Capacity (e.g., minimum age, sound mind)
4. Legality (lawful purpose) [SOURCE 1].

**Sources provided to the model:**

1. [Contract](https://www.law.cornell.edu/wex/contract) — p. 1, sha256 2053f9af7c4d… (expected)
2. [Contract](https://www.law.cornell.edu/wex/contract) — p. 1, sha256 2053f9af7c4d… (expected)
3. [Contract](https://www.law.cornell.edu/wex/contract) — p. 1, sha256 2053f9af7c4d… (expected)
4. [Contract](https://www.law.cornell.edu/wex/contract) — p. 1, sha256 2053f9af7c4d… (expected)
5. [Dodd-Frank Wall Street Reform and Consumer Protection Act](https://www.govinfo.gov/content/pkg/PLAW-111publ203/pdf/PLAW-111publ203.pdf) — p. 360, sha256 8460069ded90…

### gs-16: What is the definition of negligence, according to the Wex commentary?
- Expected document: [Negligence](https://www.law.cornell.edu/wex/negligence) (p. 1, sha256 358558607e44…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the negligence definition; the five-elements detail is consistent with the source.

**Expected answer:** Negligence is the failure to behave with the level of care that a reasonable person would have exercised under the same circumstances. Both actions and, in some cases, omissions can be found negligent -- omissions only when the person had a duty to act. Negligence is a foundational concept of tort law.

**Generated answer:** Negligence is defined as the failure to behave with the level of care that a reasonable person would have exercised under the same circumstances. It can result from a person’s actions or omissions of actions and is only considered negligent if there was a duty to act. Negligence is a foundational concept of tort law, involving several factors including the foreseeable likelihood of harm, its severity, and the burden of precautions necessary to reduce the risk of harm. The five elements typically required to prove negligence include: (1) the existence of a legal duty owed by the defendant to the plaintiff; (2) a breach of that duty; (3) harm to the plaintiff; (4) proximate cause of harm; and (5) cause-in-fact of harm to the plaintiff [SOURCE 1].

**Sources provided to the model:**

1. [Negligence](https://www.law.cornell.edu/wex/negligence) — p. 1, sha256 358558607e44… (expected)
2. [Negligence](https://www.law.cornell.edu/wex/negligence) — p. 1, sha256 358558607e44… (expected)
3. [Negligence](https://www.law.cornell.edu/wex/negligence) — p. 1, sha256 358558607e44… (expected)
4. [Negligence](https://www.law.cornell.edu/wex/negligence) — p. 1, sha256 358558607e44… (expected)
5. [Roe v. Wade](https://tile.loc.gov/storage-services/service/ll/usrep/usrep410/usrep410113/usrep410113.pdf) — p. 16, sha256 7d2f9269c16a…

### gs-17: What are the Social Security and Medicare tax rates and the Social Security wage base limit described in IRS Publication 15 (Circular E)?
- Expected document: [Publication 15 (Circular E), Employer's Tax Guide](https://www.irs.gov/pub/irs-pdf/p15.pdf) (p. 2, sha256 b46c3622439d…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the Medicare rate and SS wage base; the added 6.2% SS rate is standard and non-contradictory.

**Expected answer:** The Medicare tax rate is 1.45% each for the employee and employer, with no wage base limit for Medicare tax. The Social Security wage base limit is $184,500.

**Generated answer:** The Social Security tax rate is 6.2% for both the employee and employer, and the wage base limit for Social Security in 2026 is $184,500. The Medicare tax rate is 1.45% each for the employee and employer, and there is no wage base limit for Medicare tax [SOURCE 1].

**Sources provided to the model:**

1. [Publication 15 (Circular E), Employer's Tax Guide](https://www.irs.gov/pub/irs-pdf/p15.pdf) — p. 2, sha256 b46c3622439d… (expected)
2. [Publication 15 (Circular E), Employer's Tax Guide](https://www.irs.gov/pub/irs-pdf/p15.pdf) — p. 1, sha256 b46c3622439d… (expected)
3. [Publication 15 (Circular E), Employer's Tax Guide](https://www.irs.gov/pub/irs-pdf/p15.pdf) — p. 4, sha256 b46c3622439d… (expected)
4. [Publication 15 (Circular E), Employer's Tax Guide](https://www.irs.gov/pub/irs-pdf/p15.pdf) — p. 1, sha256 b46c3622439d… (expected)
5. [Publication 225, Farmer's Tax Guide](https://www.irs.gov/pub/irs-pdf/p225.pdf) — p. 78, sha256 67a82f92fad1…

### gs-18: What is the 2025 standard deduction for a single filer under age 65, according to IRS Publication 501?
- Expected document: [Publication 501, Dependents, Standard Deduction, and Filing Information](https://www.irs.gov/pub/irs-pdf/p501.pdf) (p. 2, sha256 288b62a4917f…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Exact match on the 2025 standard deduction figure.

**Expected answer:** For 2025, a single filer under age 65 has a standard deduction of $15,750.

**Generated answer:** The 2025 standard deduction for a single filer under age 65 is $15,750 [SOURCE 1].

**Sources provided to the model:**

1. [Publication 501, Dependents, Standard Deduction, and Filing Information](https://www.irs.gov/pub/irs-pdf/p501.pdf) — p. 2, sha256 288b62a4917f… (expected)
2. [Publication 501, Dependents, Standard Deduction, and Filing Information](https://www.irs.gov/pub/irs-pdf/p501.pdf) — p. 1, sha256 288b62a4917f… (expected)
3. [Publication 501, Dependents, Standard Deduction, and Filing Information](https://www.irs.gov/pub/irs-pdf/p501.pdf) — p. 1, sha256 288b62a4917f… (expected)
4. [Publication 501, Dependents, Standard Deduction, and Filing Information](https://www.irs.gov/pub/irs-pdf/p501.pdf) — p. 5, sha256 288b62a4917f… (expected)
5. [Publication 505, Tax Withholding and Estimated Tax](https://www.irs.gov/pub/irs-pdf/p505.pdf) — p. 14, sha256 c69e87caa93c…

### gs-19: What change did the One Big Beautiful Bill Act (OBBBA), P.L. 119-21, make to bonus depreciation according to Publication 463?
- Expected document: [Publication 463, Travel, Gift, and Car Expenses](https://www.irs.gov/pub/irs-pdf/p463.pdf) (p. 1, sha256 ddc3bb15e437…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Verified against the source: the date and 40%/60% election detail are genuinely present, not hallucinated.

**Expected answer:** OBBBA amended Internal Revenue Code section 168(k) to provide taxpayers with a permanent 100% additional first-year (bonus) depreciation deduction for qualified property acquired and placed in service, and specified plants planted or grafted, after the applicable date.

**Generated answer:** The One Big Beautiful Bill Act (OBBBA), P.L. 119-21, made several amendments to Code section 168(k) to provide taxpayers with a permanent 100% additional first-year depreciation deduction for qualified property acquired and placed in service, and specified plants planted or grafted, after January 19, 2025. This replaced the annual phasedown of the applicable percentage for the Code section 168(k) additional first-year depreciation deduction with a permanent 100% additional first-year depreciation deduction [SOURCE 1]. Additionally, OBBBA allows taxpayers to elect to deduct 40% (60% for certain property with longer production periods or certain aircraft) instead of 100% additional first-year depreciation for qualified property placed in service during the first tax year ending after January 19, 2025 [SOURCE 2].

**Sources provided to the model:**

1. [Publication 463, Travel, Gift, and Car Expenses](https://www.irs.gov/pub/irs-pdf/p463.pdf) — p. 1, sha256 ddc3bb15e437… (expected)
2. [Publication 463, Travel, Gift, and Car Expenses](https://www.irs.gov/pub/irs-pdf/p463.pdf) — p. 24, sha256 ddc3bb15e437… (expected)
3. [Publication 523, Selling Your Home](https://www.irs.gov/pub/irs-pdf/p523.pdf) — p. 1, sha256 f11fca89408f…
4. [Tax Cuts and Jobs Act](https://www.govinfo.gov/content/pkg/PLAW-115publ97/pdf/PLAW-115publ97.pdf) — p. 49, sha256 4f9ad9b1029a…
5. [Emergency Economic Stabilization Act of 2008](https://www.govinfo.gov/content/pkg/PLAW-110publ343/pdf/PLAW-110publ343.pdf) — p. 105, sha256 8bcf7509d3a4…

### gs-20: What is the self-employment (SE) tax rate for 2025, and how is it broken down, according to IRS Publication 334?
- Expected document: [Publication 334, Tax Guide for Small Business](https://www.irs.gov/pub/irs-pdf/p334.pdf) (p. 4, sha256 722639ba7bfd…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the SE tax rate breakdown; omission of the wage cap is a completeness gap, not a contradiction.

**Expected answer:** The 2025 SE tax rate on net earnings is 15.3%, consisting of 12.4% Social Security tax plus 2.9% Medicare tax. Only the first $176,100 of combined wages, tips, and net earnings is subject to the Social Security portion of SE tax in 2025.

**Generated answer:** The self-employment (SE) tax rate for 2025 is 15.3%. This is composed of 12.4% for social security tax and 2.9% for Medicare tax [SOURCE 3].

**Sources provided to the model:**

1. [Publication 334, Tax Guide for Small Business](https://www.irs.gov/pub/irs-pdf/p334.pdf) — p. 4, sha256 722639ba7bfd… (expected)
2. [Publication 334, Tax Guide for Small Business](https://www.irs.gov/pub/irs-pdf/p334.pdf) — p. 1, sha256 722639ba7bfd… (expected)
3. [Publication 334, Tax Guide for Small Business](https://www.irs.gov/pub/irs-pdf/p334.pdf) — p. 10, sha256 722639ba7bfd… (expected)
4. [Publication 334, Tax Guide for Small Business](https://www.irs.gov/pub/irs-pdf/p334.pdf) — p. 5, sha256 722639ba7bfd… (expected)
5. [Publication 334, Tax Guide for Small Business](https://www.irs.gov/pub/irs-pdf/p334.pdf) — p. 10, sha256 722639ba7bfd… (expected)

### gs-21: According to Brown v. Board of Education, what was the earlier Supreme Court doctrine that the Court's ruling on school segregation overturned, and where did that doctrine originate?
- Expected document: [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) (p. 1, sha256 7021074961cf…)
- Retrieval: hybrid=hit
- Graph-expansion expected: **Plessy v. Ferguson** — hit
- Cited expected document: True
- Judge verdict: **faithful** — Correctly identifies Plessy v. Ferguson as the overturned doctrine's origin, matching ground truth; graph expansion worked as intended.

**Expected answer:** Brown v. Board of Education overturned the 'separate but equal' doctrine that originated in Plessy v. Ferguson, 163 U.S. 537 (1896), holding that this doctrine has no place in the field of public education.

**Generated answer:** The earlier Supreme Court doctrine that the Court's ruling on school segregation in Brown v. Board of Education overturned was the "separate but equal" doctrine. This doctrine originated in the case of Plessy v. Ferguson, 163 U.S. 537, in 1896, which involved transportation rather than education [SOURCE 4].

**Sources provided to the model:**

1. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 1, sha256 7021074961cf… (expected)
2. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 4, sha256 7021074961cf… (expected)
3. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 9, sha256 7021074961cf… (expected)
4. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 9, sha256 7021074961cf… (expected)
5. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 6, sha256 7021074961cf… (expected)
6. [Plessy v. Ferguson](https://tile.loc.gov/storage-services/service/ll/usrep/usrep163/usrep163537/usrep163537.pdf) — p. 8, sha256 1bd8154d5ed6…

### gs-22: In Miranda v. Arizona, which earlier Supreme Court case did the Court rely on for the principle that appointment of counsel for indigent suspects is required?
- Expected document: [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) (p. 4, sha256 31e7666853b8…)
- Retrieval: hybrid=hit
- Graph-expansion expected: **Gideon v. Wainwright** — hit
- Cited expected document: True
- Judge verdict: **unfaithful** — Names Escobedo v. Illinois instead of Gideon v. Wainwright, the case the question specifically asked about and which was available in context (graph_hit=True) but not used.

**Expected answer:** Miranda v. Arizona ties the appointment of counsel for indigent suspects to Gideon v. Wainwright, 372 U.S. 335, alongside Douglas v. California, 372 U.S. 353.

**Generated answer:** In Miranda v. Arizona, the Court relied on the earlier Supreme Court case of Escobedo v. Illinois, 378 U. S. 478, which stressed the need for protective devices to ensure that the police interrogation process conforms to the dictates of the privilege against self-incrimination [SOURCE 5].

**Sources provided to the model:**

1. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 4, sha256 31e7666853b8… (expected)
2. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 6, sha256 31e7666853b8… (expected)
3. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 8, sha256 31e7666853b8… (expected)
4. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 1, sha256 31e7666853b8… (expected)
5. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 2, sha256 31e7666853b8… (expected)
6. [Gideon v. Wainwright](https://tile.loc.gov/storage-services/service/ll/usrep/usrep372/usrep372335/usrep372335.pdf) — p. 6, sha256 2d3219523cb2…
7. [Mapp v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep367/usrep367643/usrep367643.pdf) — p. 40, sha256 c6770815d86f…

### gs-23: What Fourth Amendment case does Miranda v. Arizona reference in discussing concerns about confessions obtained through unsupervised police interrogation?
- Expected document: [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) (p. 1, sha256 31e7666853b8…)
- Retrieval: hybrid=hit
- Graph-expansion expected: **Mapp v. Ohio** — hit
- Cited expected document: True
- Judge verdict: **unfaithful** — Names Escobedo v. Illinois instead of Mapp v. Ohio, the case the question specifically asked about and which was available in context (graph_hit=True) but not used.

**Expected answer:** Miranda v. Arizona references Mapp v. Ohio, 367 U.S. 643 (1961), in the context of Justice Harlan's dissent discussing concerns about confessions obtained at the unsupervised pleasure of the police.

**Generated answer:** Miranda v. Arizona references the case Escobedo v. Illinois, 378 U.S. 478, which stressed the need for protective devices to ensure that the process of police interrogation conforms to the dictates of the privilege against self-incrimination [SOURCE 3].

**Sources provided to the model:**

1. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 1, sha256 31e7666853b8… (expected)
2. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 6, sha256 31e7666853b8… (expected)
3. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 2, sha256 31e7666853b8… (expected)
4. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 4, sha256 31e7666853b8… (expected)
5. [Miranda v. Arizona](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384436/usrep384436.pdf) — p. 10, sha256 31e7666853b8… (expected)
6. [Gideon v. Wainwright](https://tile.loc.gov/storage-services/service/ll/usrep/usrep372/usrep372335/usrep372335.pdf) — p. 8, sha256 2d3219523cb2…
7. [Mapp v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep367/usrep367643/usrep367643.pdf) — p. 8, sha256 c6770815d86f…

### gs-24: In Regents of the University of California v. Bakke, which earlier case is cited as an example of the Court applying a lenient standard of review to a racial classification?
- Expected document: [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) (p. 5, sha256 2bd1c27f2a0f…)
- Retrieval: hybrid=hit
- Graph-expansion expected: **Korematsu v. United States** — hit
- Cited expected document: False
- Judge verdict: **faithful** — Correctly identifies Korematsu v. United States as the cited case; characterization of the point being made is a fair paraphrase, not contradictory.

**Expected answer:** Bakke cites Korematsu v. United States, 323 U.S. 214 (1944), alongside Hirabayashi v. United States, as an example where the Court sustained a racial classification even though it purported to apply a strict standard of review.

**Generated answer:** In Regents of the University of California v. Bakke, the earlier case cited as an example of the Court applying a lenient standard of review to a racial classification is **Korematsu v. United States**. The judgment refers to this case in the context of discussing the implications of judicial endorsement of racial classifications and suggests that the principles validated in Korematsu could lead to a more expansive application of racial discrimination [SOURCE 6].

**Sources provided to the model:**

1. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 5, sha256 2bd1c27f2a0f… (expected)
2. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 7, sha256 2bd1c27f2a0f… (expected)
3. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 3, sha256 2bd1c27f2a0f… (expected)
4. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 7, sha256 2bd1c27f2a0f… (expected)
5. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 31, sha256 2bd1c27f2a0f… (expected)
6. [Korematsu v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep323/usrep323214/usrep323214.pdf) — p. 33, sha256 2fdaef6d2e55…
7. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 1, sha256 7021074961cf…

### gs-25: According to Regents of the University of California v. Bakke, what series of decisions leading up to Brown v. Board of Education addressed racial segregation before Brown itself was decided?
- Expected document: Regents of the University of California v. Bakke (not among retrieved sources below)
- Retrieval: hybrid=miss
- Graph-expansion expected: **Brown v. Board of Education** — hit
- Cited expected document: False
- Judge verdict: **faithful** — Retrieval failed to surface Bakke (a genuine retrieval miss), but the model correctly declined to answer rather than fabricating content -- the desired faithful behavior given insufficient context.

**Expected answer:** Bakke references a series of decisions leading up to Brown v. Board of Education, 347 U.S. 483 (1954), including Morgan v. Virginia, Sweatt v. Painter, and McLaurin v. Oklahoma State Regents, noting that those decisions did not automatically end segregation.

**Generated answer:** The provided excerpts do not contain any information regarding the series of decisions leading up to Brown v. Board of Education, such as Regents of the University of California v. Bakke or any prior cases addressing racial segregation. Therefore, I cannot answer your question based on these sources.

**Sources provided to the model:**

1. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 1, sha256 7021074961cf…
2. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 5, sha256 7021074961cf…
3. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 4, sha256 7021074961cf…
4. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 13, sha256 7021074961cf…
5. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 10, sha256 7021074961cf…
6. [Plessy v. Ferguson](https://tile.loc.gov/storage-services/service/ll/usrep/usrep163/usrep163537/usrep163537.pdf) — p. 8, sha256 1bd8154d5ed6…

### gs-26: In Planned Parenthood v. Casey, what earlier decision does the Court reaffirm regarding the State's obligation concerning the life or health of the mother?
- Expected document: [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) (p. 2, sha256 7398a92ea959…)
- Retrieval: hybrid=hit
- Graph-expansion expected: **Roe v. Wade** — MISS
- Cited expected document: True
- Judge verdict: **faithful** — After the graph-expansion re-ranking fix, the answer now correctly names Roe v. Wade (sourced from Roe being named inline in Casey's own anchor text); graph_hit remains a technical near-miss (Roe's own chunk scored 0.032002 vs 0.032258 for the selected candidates, a statistical tie) but did not affect answer correctness.

**Expected answer:** Casey reaffirms Roe v. Wade, 410 U.S. 113 (1973), specifically its explanation of the State's obligation to protect the life or health of the mother, applying stare decisis principles to that reaffirmation.

**Generated answer:** In Planned Parenthood of Southeastern Pennsylvania v. Casey, the Court reaffirms the recognition of the State's power to restrict abortions after viability, provided that the law includes exceptions for pregnancies that endanger the woman's life or health [SOURCE 2].

**Sources provided to the model:**

1. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 1, sha256 2bd1c27f2a0f…
2. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 2, sha256 7398a92ea959… (expected)
3. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 1, sha256 2bd1c27f2a0f…
4. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 90, sha256 7398a92ea959… (expected)
5. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 2, sha256 2bd1c27f2a0f…
6. [Korematsu v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep323/usrep323214/usrep323214.pdf) — p. 33, sha256 2fdaef6d2e55…
7. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 1, sha256 7021074961cf…

### gs-27: What historically erroneous decision does Planned Parenthood v. Casey cite as an example of a doctrine that 'lasted 58 years' before being corrected?
- Expected document: [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) (p. 1, sha256 7398a92ea959…)
- Retrieval: hybrid=hit
- Graph-expansion expected: **Plessy v. Ferguson** — hit
- Cited expected document: True
- Judge verdict: **faithful** — Correctly identifies Plessy v. Ferguson and the 58-year detail, matching ground truth.

**Expected answer:** Casey cites Plessy v. Ferguson, 163 U.S. 537 (1896), as an example of an erroneous decision -- specifically its 'separate but equal' doctrine, which the opinion notes lasted 58 years after Plessy before being corrected.

**Generated answer:** Planned Parenthood v. Casey cites the decision in Plessy v. Ferguson as an example of a historically erroneous decision that "lasted 58 years" before being corrected. This case is referenced in the context of discussing how certain lines of decisional law, like that from Plessy, were overruled based on changed understandings of facts and justice [SOURCE 3].

**Sources provided to the model:**

1. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 1, sha256 7398a92ea959… (expected)
2. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 1, sha256 7398a92ea959… (expected)
3. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 4, sha256 7398a92ea959… (expected)
4. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 18, sha256 7398a92ea959… (expected)
5. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 26, sha256 7398a92ea959… (expected)
6. [Roe v. Wade](https://tile.loc.gov/storage-services/service/ll/usrep/usrep410/usrep410113/usrep410113.pdf) — p. 15, sha256 7d2f9269c16a…
7. [Plessy v. Ferguson](https://tile.loc.gov/storage-services/service/ll/usrep/usrep163/usrep163537/usrep163537.pdf) — p. 27, sha256 1bd8154d5ed6…

### gs-28: What case does Planned Parenthood v. Casey cite as an example of the Court correctly correcting one of its own errors despite a generation having grown used to the earlier decision?
- Expected document: [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) (p. 1, sha256 7398a92ea959…)
- Retrieval: hybrid=hit
- Graph-expansion expected: **Brown v. Board of Education** — hit
- Cited expected document: True
- Judge verdict: **faithful** — Graph-expansion re-ranking fix resolved this: Brown v. Board of Education now correctly appears among expanded sources (graph_hit=True), and the answer correctly names it as the case that overruled Plessy.

**Expected answer:** Casey cites Brown v. Board of Education, 347 U.S. 483 (1954), as an example where the Court corrected its error in rejecting the 'separate but equal' doctrine, alongside West Coast Hotel Co. v. Parrish overruling Adkins v. Children's Hospital.

**Generated answer:** Planned Parenthood v. Casey cites Brown v. Board of Education as an example of the Court correctly correcting one of its own errors despite a generation having grown used to the earlier decision [SOURCE 2].

**Sources provided to the model:**

1. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 1, sha256 7398a92ea959… (expected)
2. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 4, sha256 7398a92ea959… (expected)
3. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 1, sha256 7398a92ea959… (expected)
4. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 3, sha256 7398a92ea959… (expected)
5. [Planned Parenthood of Southeastern Pennsylvania v. Casey](https://tile.loc.gov/storage-services/service/ll/usrep/usrep505/usrep505833/usrep505833.pdf) — p. 18, sha256 7398a92ea959… (expected)
6. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 2, sha256 7021074961cf…
7. [Roe v. Wade](https://tile.loc.gov/storage-services/service/ll/usrep/usrep410/usrep410113/usrep410113.pdf) — p. 15, sha256 7d2f9269c16a…

### gs-29: What earlier First Amendment case does Citizens United v. FEC cite for the principle that doubt should be resolved in favor of protecting speech rather than stifling it?
- Expected document: [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) (p. 15, sha256 47426f1f570e…)
- Retrieval: hybrid=hit
- Graph-expansion expected: **New York Times Co. v. Sullivan** — hit
- Cited expected document: True
- Judge verdict: **faithful** — Correctly identifies New York Times Co. v. Sullivan matching ground truth.

**Expected answer:** Citizens United cites New York Times Co. v. Sullivan, 376 U.S. 254, 269-270 (1964), for the principle that First Amendment standards must give the benefit of any doubt to protecting rather than stifling speech.

**Generated answer:** Citizens United v. FEC cites "New York Times Co. v. Sullivan" for the principle that First Amendment standards must give the benefit of any doubt to protecting rather than stifling speech [SOURCE 2].

**Sources provided to the model:**

1. [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) — p. 15, sha256 47426f1f570e… (expected)
2. [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) — p. 18, sha256 47426f1f570e… (expected)
3. [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) — p. 22, sha256 47426f1f570e… (expected)
4. [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) — p. 2, sha256 47426f1f570e… (expected)
5. [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) — p. 3, sha256 47426f1f570e… (expected)
6. [New York Times Co. v. Sullivan](https://tile.loc.gov/storage-services/service/ll/usrep/usrep376/usrep376254/usrep376254.pdf) — p. 49, sha256 cf04431df4b6…
7. [Schenck v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep249/usrep249047/usrep249047.pdf) — p. 1, sha256 2e26f45f598e…

### gs-30: According to Citizens United v. FEC, when did the Court first consider applying the First Amendment to speech restrictions other than prior restraints, and which case marked that point?
- Expected document: [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) (p. 81, sha256 47426f1f570e…)
- Retrieval: hybrid=hit
- Graph-expansion expected: **Schenck v. United States** — hit
- Cited expected document: True
- Judge verdict: **faithful** — Correctly identifies Schenck v. United States and the 1919 date matching ground truth.

**Expected answer:** Citizens United states that the Court did not consider application of the First Amendment to speech restrictions other than prior restraints until 1919, in Schenck v. United States, 249 U.S. 47.

**Generated answer:** The Court first considered applying the First Amendment to speech restrictions other than prior restraints in 1919, as marked by the case Schenck v. United States, 249 U.S. 47 [SOURCE 1].

**Sources provided to the model:**

1. [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) — p. 81, sha256 47426f1f570e… (expected)
2. [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) — p. 3, sha256 47426f1f570e… (expected)
3. [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) — p. 2, sha256 47426f1f570e… (expected)
4. [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) — p. 26, sha256 47426f1f570e… (expected)
5. [Citizens United v. Federal Election Commission](https://tile.loc.gov/storage-services/service/ll/usrep/usrep558/usrep558310/usrep558310.pdf) — p. 20, sha256 47426f1f570e… (expected)
6. [New York Times Co. v. Sullivan](https://tile.loc.gov/storage-services/service/ll/usrep/usrep376/usrep376254/usrep376254.pdf) — p. 49, sha256 cf04431df4b6…
7. [Schenck v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep249/usrep249047/usrep249047.pdf) — p. 1, sha256 2e26f45f598e…

### gs-31: What did the Supreme Court hold in Gideon v. Wainwright regarding the right to counsel for indigent defendants in state criminal trials?
- Expected document: [Gideon v. Wainwright](https://tile.loc.gov/storage-services/service/ll/usrep/usrep372/usrep372335/usrep372335.pdf) (p. 1, sha256 2d3219523cb2…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the right-to-counsel holding and Betts v. Brady overruling; noncapital-felony detail is accurate.

**Expected answer:** The Court held that the right of an indigent defendant in a criminal trial to have the assistance of counsel is a fundamental right essential to a fair trial, and that Gideon's trial and conviction without the assistance of counsel violated the Fourteenth Amendment. The Court overruled Betts v. Brady, 316 U.S. 455, in reaching this holding.

**Generated answer:** In Gideon v. Wainwright, the Supreme Court held that the right of an indigent defendant in a criminal trial to have the assistance of counsel is a fundamental right essential to a fair trial. The Court determined that Gideon's trial and conviction without the assistance of counsel violated his rights under the Fourteenth Amendment, overruled the previous decision in Betts v. Brady, and extended the right to counsel to cases involving noncapital felonies [SOURCE 1].

**Sources provided to the model:**

1. [Gideon v. Wainwright](https://tile.loc.gov/storage-services/service/ll/usrep/usrep372/usrep372335/usrep372335.pdf) — p. 1, sha256 2d3219523cb2… (expected)
2. [Gideon v. Wainwright](https://tile.loc.gov/storage-services/service/ll/usrep/usrep372/usrep372335/usrep372335.pdf) — p. 3, sha256 2d3219523cb2… (expected)
3. [Gideon v. Wainwright](https://tile.loc.gov/storage-services/service/ll/usrep/usrep372/usrep372335/usrep372335.pdf) — p. 4, sha256 2d3219523cb2… (expected)
4. [Gideon v. Wainwright](https://tile.loc.gov/storage-services/service/ll/usrep/usrep372/usrep372335/usrep372335.pdf) — p. 5, sha256 2d3219523cb2… (expected)
5. [Gideon v. Wainwright](https://tile.loc.gov/storage-services/service/ll/usrep/usrep372/usrep372335/usrep372335.pdf) — p. 9, sha256 2d3219523cb2… (expected)

### gs-32: What did the Supreme Court hold in Mapp v. Ohio regarding evidence obtained through unconstitutional searches and seizures in state criminal trials?
- Expected document: [Mapp v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep367/usrep367643/usrep367643.pdf) (p. 1, sha256 c6770815d86f…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the exclusionary-rule holding and Wolf v. Colorado overruling.

**Expected answer:** The Court held that all evidence obtained by searches and seizures in violation of the Federal Constitution is inadmissible in a criminal trial in a state court, overruling Wolf v. Colorado, 338 U.S. 25, to the extent it held otherwise.

**Generated answer:** The Supreme Court held in Mapp v. Ohio that all evidence obtained by searches and seizures in violation of the Federal Constitution is inadmissible in a criminal trial in a state court. This ruling overruled the prior case of Wolf v. Colorado, which allowed such evidence to be used in state courts [SOURCE 1]. The Court emphasized that this exclusionary rule applies to the states through the Due Process Clause of the Fourteenth Amendment, ensuring that the right of privacy is protected in a similar manner as it is against federal officials [SOURCE 5].

**Sources provided to the model:**

1. [Mapp v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep367/usrep367643/usrep367643.pdf) — p. 1, sha256 c6770815d86f… (expected)
2. [Mapp v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep367/usrep367643/usrep367643.pdf) — p. 3, sha256 c6770815d86f… (expected)
3. [Mapp v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep367/usrep367643/usrep367643.pdf) — p. 5, sha256 c6770815d86f… (expected)
4. [Mapp v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep367/usrep367643/usrep367643.pdf) — p. 11, sha256 c6770815d86f… (expected)
5. [Mapp v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep367/usrep367643/usrep367643.pdf) — p. 13, sha256 c6770815d86f… (expected)

### gs-33: What standard did the Supreme Court apply in Terry v. Ohio to justify a police officer's pat-down search of a suspect for weapons?
- Expected document: [Terry v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep392/usrep392001/usrep392001.pdf) (p. 1, sha256 dda7b8f8fb26…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the reasonable-suspicion pat-down standard and stop/arrest distinction.

**Expected answer:** The Court held that an officer who has reasonable cause to believe that a person he is investigating is armed and dangerous may conduct a limited pat-down of the outer clothing for weapons, for his own protection, even absent probable cause to arrest.

**Generated answer:** The Supreme Court in Terry v. Ohio applied the standard of whether a police officer had "reasonable cause to believe" that the individual being investigated was armed and posed a threat of physical harm. This standard allowed the officer to take necessary measures to ensure his safety during an investigatory stop. The Court emphasized the need for swift action based on the officer's observations and experience, which warranted a limited search for weapons in the absence of probable cause for arrest [SOURCE 2], [SOURCE 4]. The Court distinguished between a "stop" and an arrest, stating that an officer can conduct a frisk of outer clothing for weapons without having probable cause to arrest, provided that the officer has a reasonable apprehension of danger based on suspicious behavior [SOURCE 3], [SOURCE 4].

**Sources provided to the model:**

1. [Terry v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep392/usrep392001/usrep392001.pdf) — p. 1, sha256 dda7b8f8fb26… (expected)
2. [Terry v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep392/usrep392001/usrep392001.pdf) — p. 3, sha256 dda7b8f8fb26… (expected)
3. [Terry v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep392/usrep392001/usrep392001.pdf) — p. 8, sha256 dda7b8f8fb26… (expected)
4. [Terry v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep392/usrep392001/usrep392001.pdf) — p. 2, sha256 dda7b8f8fb26… (expected)
5. [Terry v. Ohio](https://tile.loc.gov/storage-services/service/ll/usrep/usrep392/usrep392001/usrep392001.pdf) — p. 7, sha256 dda7b8f8fb26… (expected)

### gs-34: What did the Supreme Court hold in Tinker v. Des Moines Independent Community School District regarding students wearing armbands to school as a form of protest?
- Expected document: [Tinker v. Des Moines Independent Community School District](https://tile.loc.gov/storage-services/service/ll/usrep/usrep393/usrep393503/usrep393503.pdf) (p. 1, sha256 9e2abaf1ba82…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the student-speech holding and the material-and-substantial-interference standard.

**Expected answer:** The Court held that the students' wearing of black armbands to protest the Vietnam War was quiet, passive, non-disruptive conduct protected by the Free Speech Clause of the First Amendment and the Due Process Clause of the Fourteenth Amendment, and that students do not shed their constitutional rights to freedom of speech at the schoolhouse gate.

**Generated answer:** The Supreme Court held that students wearing armbands to protest the government's policy in Vietnam were engaging in conduct protected by the Free Speech Clause of the First Amendment and the Due Process Clause of the Fourteenth Amendment. Specifically, the Court found that the students' act of wearing the armbands was quiet and passive, and did not disrupt school activities or impinge upon the rights of others. The Court stated that a prohibition against expression of opinion is not permissible unless it can be shown that such expression would materially and substantially interfere with the operation of the school or the rights of other students. In this case, there was no evidence of such interference, which led to the reversal of the lower courts' decisions [SOURCE 1][SOURCE 4].

**Sources provided to the model:**

1. [Tinker v. Des Moines Independent Community School District](https://tile.loc.gov/storage-services/service/ll/usrep/usrep393/usrep393503/usrep393503.pdf) — p. 1, sha256 9e2abaf1ba82… (expected)
2. [Tinker v. Des Moines Independent Community School District](https://tile.loc.gov/storage-services/service/ll/usrep/usrep393/usrep393503/usrep393503.pdf) — p. 3, sha256 9e2abaf1ba82… (expected)
3. [Tinker v. Des Moines Independent Community School District](https://tile.loc.gov/storage-services/service/ll/usrep/usrep393/usrep393503/usrep393503.pdf) — p. 2, sha256 9e2abaf1ba82… (expected)
4. [Tinker v. Des Moines Independent Community School District](https://tile.loc.gov/storage-services/service/ll/usrep/usrep393/usrep393503/usrep393503.pdf) — p. 7, sha256 9e2abaf1ba82… (expected)
5. [Tinker v. Des Moines Independent Community School District](https://tile.loc.gov/storage-services/service/ll/usrep/usrep393/usrep393503/usrep393503.pdf) — p. 2, sha256 9e2abaf1ba82… (expected)

### gs-35: What did the Supreme Court hold in Roe v. Wade regarding a woman's constitutional right of privacy and the decision to terminate a pregnancy?
- Expected document: [Roe v. Wade](https://tile.loc.gov/storage-services/service/ll/usrep/usrep410/usrep410113/usrep410113.pdf) (p. 1, sha256 7d2f9269c16a…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the right-of-privacy holding and its Fourteenth/Ninth Amendment grounding.

**Expected answer:** The Court held that the constitutional right of privacy, whether founded in the Fourteenth Amendment's concept of personal liberty or the Ninth Amendment's reservation of rights to the people, is broad enough to encompass a woman's decision whether or not to terminate her pregnancy.

**Generated answer:** The Supreme Court held that the Texas criminal abortion statutes are unconstitutional because they improperly invade a woman's right to choose to terminate her pregnancy. This right was found to be rooted in the concept of personal "liberty" as embodied in the Due Process Clause of the Fourteenth Amendment, and in the personal, marital, familial, and sexual privacy protected by the Bill of Rights, including the Ninth Amendment [SOURCE 2][SOURCE 4]. The Court affirmed that Roe and the physician, Hallford, had standing to challenge the Texas laws, and emphasized that the fundamental right to choose whether to have children is protected by the Constitution [SOURCE 4].

**Sources provided to the model:**

1. [Roe v. Wade](https://tile.loc.gov/storage-services/service/ll/usrep/usrep410/usrep410113/usrep410113.pdf) — p. 1, sha256 7d2f9269c16a… (expected)
2. [Roe v. Wade](https://tile.loc.gov/storage-services/service/ll/usrep/usrep410/usrep410113/usrep410113.pdf) — p. 3, sha256 7d2f9269c16a… (expected)
3. [Roe v. Wade](https://tile.loc.gov/storage-services/service/ll/usrep/usrep410/usrep410113/usrep410113.pdf) — p. 17, sha256 7d2f9269c16a… (expected)
4. [Roe v. Wade](https://tile.loc.gov/storage-services/service/ll/usrep/usrep410/usrep410113/usrep410113.pdf) — p. 10, sha256 7d2f9269c16a… (expected)
5. [Roe v. Wade](https://tile.loc.gov/storage-services/service/ll/usrep/usrep410/usrep410113/usrep410113.pdf) — p. 13, sha256 7d2f9269c16a… (expected)

### gs-36: What standard did the Supreme Court establish in New York Times Co. v. Sullivan for public officials seeking damages for defamatory statements about their official conduct?
- Expected document: [New York Times Co. v. Sullivan](https://tile.loc.gov/storage-services/service/ll/usrep/usrep376/usrep376254/usrep376254.pdf) (p. 2, sha256 cf04431df4b6…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the actual-malice standard precisely.

**Expected answer:** The Court held that a public official cannot recover damages for a defamatory falsehood relating to their official conduct unless they prove the statement was made with 'actual malice' -- that is, with knowledge that it was false or with reckless disregard of whether it was false or not.

**Generated answer:** The Supreme Court established that a public official must prove "actual malice" to seek damages for defamatory statements concerning their official conduct. Actual malice is defined as knowledge that the statements are false or a reckless disregard for the truth. This standard is necessary for an award of damages for false statements, and the Court ruled that simply showing factual error or defamatory content is insufficient unless actual malice is alleged and proved [SOURCE 1].

**Sources provided to the model:**

1. [New York Times Co. v. Sullivan](https://tile.loc.gov/storage-services/service/ll/usrep/usrep376/usrep376254/usrep376254.pdf) — p. 2, sha256 cf04431df4b6… (expected)
2. [New York Times Co. v. Sullivan](https://tile.loc.gov/storage-services/service/ll/usrep/usrep376/usrep376254/usrep376254.pdf) — p. 1, sha256 cf04431df4b6… (expected)
3. [New York Times Co. v. Sullivan](https://tile.loc.gov/storage-services/service/ll/usrep/usrep376/usrep376254/usrep376254.pdf) — p. 10, sha256 cf04431df4b6… (expected)
4. [New York Times Co. v. Sullivan](https://tile.loc.gov/storage-services/service/ll/usrep/usrep376/usrep376254/usrep376254.pdf) — p. 8, sha256 cf04431df4b6… (expected)
5. [New York Times Co. v. Sullivan](https://tile.loc.gov/storage-services/service/ll/usrep/usrep376/usrep376254/usrep376254.pdf) — p. 14, sha256 cf04431df4b6… (expected)

### gs-37: What did the Supreme Court hold in Korematsu v. United States regarding the wartime exclusion order affecting persons of Japanese ancestry?
- Expected document: [Korematsu v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep323/usrep323214/usrep323214.pdf) (p. 2, sha256 2fdaef6d2e55…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the conviction-affirmed holding; the narrower scope description (exclusion vs. detention orders) is consistent with the actual opinion.

**Expected answer:** The Court affirmed Korematsu's conviction, holding that the exclusion order under which he was convicted was valid even though evacuation and detention in an assembly center were inseparable from the exclusion itself.

**Generated answer:** The Supreme Court held that Civilian Exclusion Order No. 34, which directed the exclusion of all persons of Japanese ancestry from a designated military area during wartime as a protection against espionage and sabotage, was constitutional at the time it was made. This ruling pertained specifically to the case where the petitioner, an American citizen of Japanese descent, violated this order by remaining in the prohibited area [SOURCE 2]. The Court acknowledged the hardships imposed by the exclusion on American citizens but stated that such hardships are part of the realities of war, emphasizing the responsibilities of citizenship in wartime [SOURCE 3]. The validity of other orders that required detention in assembly or relocation centers was not considered in this proceeding [SOURCE 2].

**Sources provided to the model:**

1. [Korematsu v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep323/usrep323214/usrep323214.pdf) — p. 2, sha256 2fdaef6d2e55… (expected)
2. [Korematsu v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep323/usrep323214/usrep323214.pdf) — p. 1, sha256 2fdaef6d2e55… (expected)
3. [Korematsu v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep323/usrep323214/usrep323214.pdf) — p. 6, sha256 2fdaef6d2e55… (expected)
4. [Korematsu v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep323/usrep323214/usrep323214.pdf) — p. 4, sha256 2fdaef6d2e55… (expected)
5. [Korematsu v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep323/usrep323214/usrep323214.pdf) — p. 8, sha256 2fdaef6d2e55… (expected)

### gs-38: What did the Supreme Court hold in Gibbons v. Ogden regarding the scope of Congress's power to regulate commerce among the states?
- Expected document: [Gibbons v. Ogden](https://tile.loc.gov/storage-services/service/ll/usrep/usrep022/usrep022001/usrep022001.pdf) (p. 162, sha256 59b99d503c94…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Accurately describes a real part of the holding (commerce includes navigation, Supremacy Clause preemption); different emphasis than the reference but not contradictory.

**Expected answer:** The Court held that Congress's power over commerce with foreign nations and among the several states is as plenary and absolute, within its specified objects, as it would be in a single unified government, subject only to the restrictions found in the Constitution itself.

**Generated answer:** In Gibbons v. Ogden, the Supreme Court held that Congress has the power to regulate commerce, which is understood to include navigation. The Court determined that the regulation of commerce must encompass activities that take place among the several states, and that both state and federal laws cannot be in conflict concerning such regulation. If federal law is made in the lawful exercise of its power and conflicts with state law, the state law must be void due to this repugnancy [SOURCE 5].

**Sources provided to the model:**

1. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 1, sha256 2bd1c27f2a0f…
2. [United States v. Lopez](https://tile.loc.gov/storage-services/service/ll/usrep/usrep514/usrep514549/usrep514549.pdf) — p. 45, sha256 4bd8c017a148…
3. [Regents of the University of California v. Bakke](https://tile.loc.gov/storage-services/service/ll/usrep/usrep438/usrep438265/usrep438265.pdf) — p. 1, sha256 2bd1c27f2a0f…
4. [United States v. Lopez](https://tile.loc.gov/storage-services/service/ll/usrep/usrep514/usrep514549/usrep514549.pdf) — p. 20, sha256 4bd8c017a148…
5. [Gibbons v. Ogden](https://tile.loc.gov/storage-services/service/ll/usrep/usrep022/usrep022001/usrep022001.pdf) — p. 162, sha256 59b99d503c94… (expected)
6. [Korematsu v. United States](https://tile.loc.gov/storage-services/service/ll/usrep/usrep323/usrep323214/usrep323214.pdf) — p. 1, sha256 2fdaef6d2e55…
7. [Brown v. Board of Education](https://tile.loc.gov/storage-services/service/ll/usrep/usrep347/usrep347483/usrep347483.pdf) — p. 2, sha256 7021074961cf…

### gs-39: What principle did the Supreme Court establish in McCulloch v. Maryland regarding a state's power to tax an instrumentality of the federal government?
- Expected document: [McCulloch v. Maryland](https://tile.loc.gov/storage-services/service/ll/usrep/usrep017/usrep017316/usrep017316.pdf) (p. 2, sha256 b0496fefea52…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the power-to-tax-is-power-to-destroy holding with a direct quote.

**Expected answer:** The Court held that the power to tax involves the power to destroy, and that a state may not tax an instrumentality of the federal government such as the Bank of the United States, because doing so would allow one government to control and potentially defeat the constitutional measures of another government that is supreme over it.

**Generated answer:** The Supreme Court established that states do not have the power to tax instruments of the federal government, asserting that "the States have no power, by taxation, or otherwise, to retard, impede, burden, or in any manner control the operations of the constitutional laws enacted by Congress" [SOURCE 1]. The Court reasoned that permitting states to impose taxes could undermine the federal government’s operations, as it would allow states to interfere with federal entities like the Bank of the United States [SOURCE 3]. This principle emphasizes the supremacy of federal law and the need to prevent state interference with federal powers [SOURCE 2].

**Sources provided to the model:**

1. [McCulloch v. Maryland](https://tile.loc.gov/storage-services/service/ll/usrep/usrep017/usrep017316/usrep017316.pdf) — p. 2, sha256 b0496fefea52… (expected)
2. [McCulloch v. Maryland](https://tile.loc.gov/storage-services/service/ll/usrep/usrep017/usrep017316/usrep017316.pdf) — p. 1, sha256 b0496fefea52… (expected)
3. [McCulloch v. Maryland](https://tile.loc.gov/storage-services/service/ll/usrep/usrep017/usrep017316/usrep017316.pdf) — p. 13, sha256 b0496fefea52… (expected)
4. [McCulloch v. Maryland](https://tile.loc.gov/storage-services/service/ll/usrep/usrep017/usrep017316/usrep017316.pdf) — p. 29, sha256 b0496fefea52… (expected)
5. [McCulloch v. Maryland](https://tile.loc.gov/storage-services/service/ll/usrep/usrep017/usrep017316/usrep017316.pdf) — p. 5, sha256 b0496fefea52… (expected)

### gs-40: What did the Supreme Court hold in Bush v. Gore regarding the manual recount of ballots ordered by the Florida Supreme Court?
- Expected document: [Bush v. Gore](https://tile.loc.gov/storage-services/service/ll/usrep/usrep531/usrep531098/usrep531098.pdf) (p. 3, sha256 ff42d63809ba…)
- Retrieval: hybrid=hit
- Cited expected document: True
- Judge verdict: **faithful** — Matches the equal-protection and safe-harbor-deadline holding.

**Expected answer:** The Court held that the recount procedures ordered by the Florida Supreme Court, lacking uniform standards for determining voter intent across counties, violated the Equal Protection Clause, and that no constitutionally valid recount could be completed by the December 12 safe-harbor deadline.

**Generated answer:** The Supreme Court held that the manual recounts ordered by the Florida Supreme Court were unconstitutional under the Equal Protection Clause. They stated that any recount aimed at meeting the December 12 "safe-harbor" date would violate the Equal Protection Clause because it required uniform treatment of votes. The Supreme Court further determined that the Florida Supreme Court's judgment ordering manual recounts was reversed [SOURCE 4].

**Sources provided to the model:**

1. [Bush v. Gore](https://tile.loc.gov/storage-services/service/ll/usrep/usrep531/usrep531098/usrep531098.pdf) — p. 3, sha256 ff42d63809ba… (expected)
2. [Bush v. Gore](https://tile.loc.gov/storage-services/service/ll/usrep/usrep531/usrep531098/usrep531098.pdf) — p. 5, sha256 ff42d63809ba… (expected)
3. [Bush v. Gore](https://tile.loc.gov/storage-services/service/ll/usrep/usrep531/usrep531098/usrep531098.pdf) — p. 4, sha256 ff42d63809ba… (expected)
4. [Bush v. Gore](https://tile.loc.gov/storage-services/service/ll/usrep/usrep531/usrep531098/usrep531098.pdf) — p. 1, sha256 ff42d63809ba… (expected)
5. [Bush v. Gore](https://tile.loc.gov/storage-services/service/ll/usrep/usrep531/usrep531098/usrep531098.pdf) — p. 5, sha256 ff42d63809ba… (expected)
