# Binayak Gurubacharya — Ukiyo / Watermelon Nerd

A locally reviewable update to the original HTML, CSS and JavaScript portfolio. It preserves the night-sky opening, pink accents, local Poppins/Lora fonts, Ukiyo identity, and personal photograph. No packages, service accounts or external font services are needed.

## Run locally

From this folder:

```sh
python3 scripts/preview.py
```

Open http://127.0.0.1:8765. Stop the server with Ctrl+C. For another port, use `python3 scripts/preview.py --port 8766`.

The preview builds `dist/` first and serves only those public files. After editing source files, run `python3 scripts/build.py` again and refresh the browser. Alternatively, stop and restart the preview.

With Node/npm available, equivalent commands are `npm run dev`, `npm run check`, and `npm run build`. There is no dependency installation step.

## Check and build

```sh
python3 scripts/check.py
node --check js/portfolio.js
python3 scripts/build.py
```

`dist/` is generated from the HTML and CSS asset references. It excludes the legacy style demo, PHP contact handler, old plugins, scripts, research notes and the original private resume. Nothing has been deployed.

## Edit

- `index.html`: content, project descriptions, links and section order.
- `css/portfolio.css`: responsive layout, typography, theme and reduced-motion behavior.
- `js/portfolio.js`: mobile navigation, section highlighting and email copying.
- `downloads/Binayak_Gurubacharya_Resume.pdf`: public resume with no phone number and corrected contact/project links.
- `scripts/create_public_resume.py`: reproducible public resume source (optional; requires ReportLab).
- `docs/content-review.md`: source evidence and consolidated second-pass questions.
- `docs/verification.md`: checks performed and practical verification limits.

The original fonts, images, legacy CSS/JS, style demo, and template license remain in the working folder. The public site omits the artwork gallery and hero artwork; Shattered and Puzzle remain available as source assets for optional future use. The updated page loads only the new CSS and JS. The old AJAX contact form was replaced with direct email and a copy action; no email is sent by this site.

## Accessibility and behavior

Semantic sections and headings, a skip link, visible keyboard focus, a mobile menu with expanded state and Escape support, native education and additional-project disclosures. Navigation and content remain usable without JavaScript. Motion is limited to scrolling and hover transitions, with reduced-motion overrides. Project visuals are labeled concept diagrams, not screenshots or claims of a running demo.

## Attribution

Original Kards template by [Styleshout](https://www.styleshout.com/). Its attribution is retained in the site footer. See `readme.txt` for the original license and credits.
