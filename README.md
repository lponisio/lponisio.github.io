# Ponisio Lab — GitHub Pages migration

This is a zero-build static website designed to replace the current Weebly site. It is intentionally simple and academic in style: a concise homepage, lightweight navigation, and separate pages for research, people, publications, open science, joining the lab, and media.

## What was migrated

- Core lab description and research framing
- Five major research areas from the current site
- Current lab-member bios and alumni list
- Publication list visible on the current site (reformatted and lightly cleaned)
- NIMBLE / reproducible-science material
- Lab mission/advice/expectations links
- 2026 graduate-student admissions status and joining information
- Media / lab-happenings archive
- Research figures and images that could be identified from the public Weebly site
- Existing `www.ponisiolab.com` custom-domain name via the included `CNAME` file

The old homepage's long media excerpts were deliberately moved to `media.html` to make the homepage much closer to the compact academic-home-page style you referenced.

## IMPORTANT: preserve images before cancelling Weebly

The draft HTML currently references image files hosted by Weebly. Before closing the Weebly account, run this from the repository directory on a computer with internet access:

```bash
python3 scripts/localize_weebly_assets.py
```

It uses only Python's standard library. It downloads the Weebly-hosted images/PDFs that were discovered and automatically rewrites the HTML to point to local copies. Commit those downloaded files to GitHub before cancelling Weebly.

See `ASSET_MANIFEST.md` for details.

## Easiest GitHub Pages setup

Lauren's GitHub username is `lponisio`, so the cleanest setup is a public repository named exactly:

```text
lponisio.github.io
```

Then:

1. Upload the **contents** of this folder to that repository (not the enclosing folder itself).
2. Commit/push to the `main` branch.
3. In GitHub, open **Settings → Pages**.
4. Choose **Deploy from a branch**, `main`, `/ (root)`.
5. The site should first appear at `https://lponisio.github.io/`.
6. Once you are happy with it, set the custom domain to `www.ponisiolab.com` in GitHub Pages and update the domain's DNS records away from Weebly and toward GitHub Pages.
7. Only cancel Weebly after the local image migration and DNS cutover are confirmed.

The included `.nojekyll` file tells GitHub Pages to serve the site exactly as-is; there is no theme or build dependency to maintain.

## Editing

All pages are ordinary HTML files at the repository root. The visual design lives in:

```text
assets/css/style.css
```

The responsive mobile navigation is in:

```text
assets/js/nav.js
```

Because there is no framework, there is very little that can break. Content can be edited directly in GitHub's web editor.

## Files worth reviewing before launch

- `index.html` — homepage wording and contact block
- `people.html` — current members and statuses
- `publications.html` — migrated publication list
- `join.html` — time-sensitive 2026 admissions language
- `media.html` — media links (some are intentionally general outlet links and can be replaced with exact article URLs)
- `resources.html` — placeholder for infographic / ID-guide files that were not exposed to the crawler
- `CNAME` — currently set to `www.ponisiolab.com`

## Design choices

The design borrows the *approach* of Carl Boettiger's site rather than copying it: ample whitespace, restrained typography, a compact PI/contact card, and a strong separation between the homepage and detailed material. It also retains some Ponisio Lab identity through the existing logo and muted blue/mauve accents.

## Existing links / search results

Redirect pages are included for the old Weebly URLs (`members.html`, `join-the-lab.html`, individual project pages, `nimble.html`, `reproducible-science.html`, `lab-happenings.html`, etc.), so links already circulating on the web will continue to land in the right part of the new site after the domain moves.
