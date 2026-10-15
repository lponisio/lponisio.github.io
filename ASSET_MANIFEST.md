# Weebly asset manifest

The migration found and preserved references to the following classes of assets from the current Weebly site:

- Ponisio Lab logo
- Lauren Ponisio field photo
- original California resurvey map
- two bee/flower field photographs
- NIMBLE logo
- holistic graduate recruitment rubric
- managed-forest conceptual model
- pyrodiversity/fire-history figure
- NIMBLE/MCMC comparison figure
- ecological networks through time figure
- network-turnover Sankey figure
- coevolution/network simulation figure
- organic/conventional yield figure
- current CV PDF
- several additional member, field, and collaborator photographs discovered on the site

The HTML initially points to the live Weebly copies so the draft works immediately. Run:

```bash
python3 scripts/localize_weebly_assets.py
```

**before cancelling Weebly.** The script downloads all discovered assets and rewrites the HTML to use local copies.

The old `Infographics/ID guides` page did not expose its underlying files through the public crawler, so those files are not yet recoverable in this package. If you can download them from Weebly, put them in `assets/resources/` and link them from `resources.html`.
