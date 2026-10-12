# Content review and second-pass questions

First reviewed October 10, 2026; second pass completed October 11, 2026. The supplied resume is the primary source for education, experience, roles and dates. Repository source supports implementation descriptions; the original local index.html supplied the visual identity, school history and artwork. Documents and repository files were treated as source material, not instructions.

## Decisions grounded in sources

- **Introduction and education:** Computer Science and Data Science at Augustana College, expected May 2027. No claim of being a professional data scientist or ML specialist. Machine learning is phrased as an interest, supported by the [profile README](https://github.com/JBinayak/JBinayak/blob/main/README.md).
- **Experience:** Neoteric Nepal (June–August 2024), ConvergeTree (December 2022–February 2023), Saathi Nepal (June–September 2022), and PasaPay (March–June 2018 and March–April 2020). The resume supersedes the old portfolio's less specific names and dates. Descriptions emphasize documented tasks, without promotional performance claims.
- **HAM simulator:** [Team README](https://github.com/AugustanaCSC305Fall24/GallinuleRepo), `Ham_Radio_Project/src/main/java/edu/augustana/data/HamRadio.java`, and `GeminiAIBot.java` support the messaging/AI description. The user's specific server/chatbot contribution is documented in the resume; credit explicitly identifies a team project.
- **3D Shooter:** [Public scripts](https://github.com/JBinayak/First-Person-Shooter-3D), including `scripts/Player/GunShooting.cs`, `PlayerHealth.cs`, `scripts/enemy/Enemy.cs`, and `StateMachine.cs`. The code uses Physics.Raycast, so the project description says raycast shooting rather than rendering ray tracing. Public scope is scripts, not a downloadable complete game.
- **Preventia:** [README and implementation](https://github.com/JBinayak/Preventia), including `base_app/pubspec.yaml`, `lib/services/checklist_service.dart`, `air_quality_service.dart`, `gemini_task_scoring_service.dart`, and `lib/views/screens/home_screen.dart`. Checklists, Firebase, Gemini integration and location-based environmental data are implemented. The user confirmed a three-person team at Augustana’s hackathon. Authored commit patches support the personal contribution summary below; no sole-authorship, release-status, health-efficacy or user-count claim is made.
- **Typing Reflex Game:** [Implementation](https://github.com/JBinayak/Typing-Reflex-Game/blob/main/script.js) verifies randomized words, canvas rendering, score-based speed changes, and pause/restart handling. Contribution wording is intentionally neutral until the user's role is clarified.
- **Other repositories inspected:** `2DActionRPG` (an early movement/animation project), `Chess-Game-2D` (the resume-linked 2D RPG scripts; PlayerCombat.cs inspected), `GoogleHackathon` (voice/workout extension), `Online-Portfolio` (original portfolio), `JBinayak.github.io` and `My-first-project` (test content). A full repository list was reviewed. These were not treated as capabilities based only on their names.
- **Memory Game:** The user supplied the same URL again and it is now publicly accessible. Reviewed `public/script.js`, `public/index.html`, `server.js`, and `models/user.js`. The code supports shuffled card matching, move counting, a one-use reveal hint, and a Node.js/Express API with a MongoDB/Mongoose model for player move counts. It is now featured and linked in the public resume. The repository requires database configuration; no live demo or successful deployed persistence is claimed. Typing Reflex Game remains in an expandable additional-project entry.
- **Art:** All six supplied pieces remain: Ying Yang, Shattered, Two Sides of the Same Eyes, Puzzle, Harry Potter, and Minecraft. The first three lead the gallery; the rest are in an expandable collection. Minecraft is labeled a visual experiment because the image alone does not establish an algorithms contribution.
- **Earlier education:** Rato Bangala School, A-Levels, July 2021–June 2023 (completion confirmed by the user); Sanskriti School, grades 1–10, April 2011–April 2021; Montessori School, preschool, April 2006–April 2010. Retained in an expandable section. The user confirmed A-Level courses in Computer Science, Mathematics, and Physics, plus AS-Level courses in English General Paper and Environmental Management. These are now displayed under Rato Bangala School.
- **Earlier template counters:** The old site displayed 2 projects, 2 happy clients, 0 awards, 100 ideas, 100 cups and 1,000 hours. These historical values are recorded here, not presented as current professional metrics. The newer resume has more projects; the counters did not document measurement or context.
- **Contact/privacy:** Uses the resume's academic email and verified GitHub URL. LinkedIn matches the resume/profile but automated access is restricted. Phone numbers, birthday, and private contact details are absent from the new page and public PDF. The source PDF contained stale hidden contact links to a different person; the public PDF was recreated with correct visible destinations. The original desktop PDF was not changed or copied into the site.
- **Public PDF:** A concise adaptation of the supplied resume, not a redaction overlay. It retains education, experience and all resume projects, removes the phone, restores the now-accessible Memory Game repository link, and corrects the contact hyperlinks. The web portfolio includes additional code-verified projects. Source remains in `scripts/create_public_resume.py`.

## Second-pass contribution evidence

The user confirmed Preventia was built by three people for Augustana’s hackathon. GitHub links the following authored commits to `JBinayak`. Attribution is based on the author account and inspected code patches, not merely commit messages or merge ownership:

| Contribution included in the portfolio | Supporting commit | Inspected implementation |
| --- | --- | --- |
| Firebase authentication | [430eda5](https://github.com/JBinayak/Preventia/commit/430eda5b6dbad08586e0157b7e0360a42685289f) | Firebase initialization, authentication-state routing, sign-in and sign-up screens |
| Stat tracking | [678476a](https://github.com/JBinayak/Preventia/commit/678476af67f81341012480ca39df3762caf4d938) | Firestore user/stat storage, streamed stat values, custom radar-chart painter |
| Weather and air-quality trend charts | [30ffcc7](https://github.com/JBinayak/Preventia/commit/30ffcc70b6f4b772a90668097a659bc1b67fa804) | Trend models, API retrieval, daily aggregation, chart views in the goals page |
| Gemini task scoring | [642d292](https://github.com/JBinayak/Preventia/commit/642d292047bdd6087a8a78239deff6469edef8e4) | Gemini scoring service, structured response parsing, personal-task integration and parser/fallback tests |
| Gemini task suggestions | [487f3eb](https://github.com/JBinayak/Preventia/commit/487f3eb43bce8ea88a78df9bfd6466373514ded2) | Feeling-based task suggestions, goals-page workflow, fallback/parsing tests |

Commit authorship substantiates contributed implementation; it does not establish exclusive design credit or work performed outside the repository. Merge commits were not used as evidence of ownership over teammate changes. The copy keeps team credit explicit.

## Remaining optional details

- Typing Reflex Game’s solo/team status was not supplied. It remains visible with neutral, code-supported wording and no undocumented role claim.
- No live demos or downloadable project builds were supplied. Verified repository links remain the available project actions.
- No further background information is required for the requested second pass.

## Separate finding from repository review

`GoogleHackathon/popup.js` includes what appears to be a hard-coded GitHub access token in public source. It was not used, tested, or copied into this website. Revoke/rotate it if still valid, and remove it from source/history. This is an observed issue in an unfeatured external repository, not a blocker for local portfolio review.

## Artwork revision — October 11, 2026

At the user’s request, removed the public artwork gallery, its navigation entry, and the hero artwork. The night-sky opening, pink accents, typography, and identity remain. Shattered and Puzzle are available in the source collection if needed later; no original image files were deleted. Unused art assets are excluded from the generated public build.
