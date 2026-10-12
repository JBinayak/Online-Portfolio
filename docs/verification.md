# Verification — October 10, 2026

## Completed

- `npm run check`: local file links, anchor IDs, one primary heading, image alternatives, known private/stale content checks, CSS asset existence and JavaScript syntax all passed.
- `npm run build`: generated an explicit allowlist of public site assets in `dist/`; no dependencies needed.
- HTTP 200 for every built asset, including fonts, images, JavaScript, CSS and resume.
- Four featured repositories and GitHub profile returned HTTP 200. Styleshout credit returned HTTP 200.
- Browser resume download completed successfully from the hero link.
- Public PDF: rendered and visually inspected at 1400px; one page; no clipping; no phone number or stale hidden contact links; seven link annotations inspected. Source PDF left unchanged.
- Desktop review at 1440×1000; tablet at 768×1024; mobile at 390×844 and 320×740. No horizontal overflow. Header, hero, project feature, timeline, education disclosure, artwork modal and contact section visually inspected.
- Navigation reaches matching anchors with sticky-header clearance. Mobile menu opens, closes after selecting a destination, closes with Escape, and restores focus to its toggle. Selecting a section on mobile focuses its destination.
- Artwork dialog: open, forward/reverse Tab wrap, Escape dismissal, focus restoration, and scroll unlock verified.
- Email copy action confirmed its success status in the browser. Email link uses the correct `mailto:` destination; no message was sent.
- Page console reported no warnings or errors during the updated-page inspection.
- Key text color pairs measured above 4.5:1 contrast. CSS includes visible focus styles and reduced-motion overrides. No automatic animation, preloader, autoplay audio or background network widgets.

## Limits

- LinkedIn returned HTTP 999 to automated requests; the URL is taken from the supplied resume and GitHub profile. Its public profile rendering could not be independently verified.
- Reduced-motion behavior was reviewed in CSS; no OS-level preference was changed during testing. No full screen-reader or assistive-technology certification is claimed.
- This is a static portfolio. Featured projects were reviewed as source; they were not compiled or run, and concept diagrams are not product screenshots.
- No deployment, publication or external message was performed.

## Second pass — October 11, 2026

- Reviewed authored Preventia commit patches and linked the supporting commits in `content-review.md`; copy now explicitly credits a three-person Augustana hackathon team and the user's documented implementation work.
- Updated Rato Bangala School to July 2021–June 2023, A-Levels, with the user-confirmed A-Level and AS-Level courses. Expanded education disclosure checked visually.
- Reviewed Memory Game client logic, Express endpoints, and Mongoose model. Promoted it to a featured project; retained Typing Reflex Game in an additional-project disclosure. Repository returned HTTP 200.
- `npm run check` passed with 43 references and 22 unique IDs; `npm run build` produced 24 public files.
- Revised Memory Game project, Preventia copy, and education disclosure reviewed at desktop/mobile sizes; no horizontal overflow at 390px or 320px. New project disclosure expands and exposes its working source link. Browser console showed no errors or warnings.
- Regenerated and rendered the public PDF: one page, eight inspected link annotations, restored Memory Game link, no clipping. Local resume request returned HTTP 200.
- Screenshots saved under `output/review/`; no deployment or publication performed.

## Artwork removal — October 11, 2026

- Removed the gallery, hero artwork, Off the clock navigation entry, and the artwork dialog and associated styles/scripts. Contact now follows Journey and is numbered 04. Original image files remain in source; none are shipped in the current build.
- `npm run check` passed (28 references, 15 unique IDs); `npm run build` produced 12 public files.
- Reviewed desktop at 1440px and mobile at 390px; no horizontal overflow at 1440px, 390px, or 320px. Mobile menu opens, its contact link closes the menu and moves focus to Contact.
- Browser testing caught a cached copy of the old dialog script; versioned CSS/JS URLs resolved it. The fresh script reaches email-copy setup and introduces no new console errors. Earlier cached-script errors remain in the browser's log history.
- Saved `output/review/no-art-desktop.jpg` and `output/review/no-art-mobile.jpg`. Restored the browser viewport and left the existing user preview server running. No deployment or publication.
