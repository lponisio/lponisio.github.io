#!/usr/bin/env python3
"""One-time Weebly asset migration.

Run this while www.ponisiolab.com is still live. It downloads the image/PDF
assets discovered during the migration and replaces their Weebly URLs in the
HTML with local relative paths, making the GitHub Pages site self-contained.

Usage:
    python3 scripts/localize_weebly_assets.py
"""
from pathlib import Path
from urllib.request import Request, urlopen
import time

ROOT = Path(__file__).resolve().parents[1]

ASSETS = {
    # used by the new site
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/ponisiolab_orig.png": "assets/images/ponisiolab-logo.png",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/published/lauren-ponisio1.jpeg?1610395858=": "assets/images/lauren-ponisio.jpeg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/ca-map-original-moldanke_orig.jpg": "assets/images/california-original-survey-map.jpg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/img-3806.jpg": "assets/images/bee-yellow-flower.jpg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/img-4012.jpg": "assets/images/bee-pink-flower.jpg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/nimblelogo_orig.png": "assets/images/nimble-logo.png",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/editor/example-rubric.png?1630957265=": "assets/images/holistic-recruitment-rubric.png",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/conceptual_orig.png": "assets/images/forest-conceptual-model.png",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/pyrodiv2_orig.jpg": "assets/images/pyrodiversity-figure.jpg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/ece36053-fig-0001-m_orig.png": "assets/images/nimble-mcmc-figure.png",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/published/yearnetsdegree.jpg?1548908451=": "assets/images/network-through-time.jpg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/editor/sankeyidb303b2e99ce.jpg?1500573276=": "assets/images/network-turnover-sankey.jpg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/methods_orig.jpeg": "assets/images/coevolution-network-methods.jpeg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/published/fig2.jpg?1500573295=": "assets/images/organic-yield-figure.jpg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/lcp_cv.pdf": "assets/files/lcp_cv.pdf",

    # additional assets found on the current site; kept so they are not lost
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/published/natgeo2.jpeg?1632759677=": "assets/images/archive-member-01.jpeg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/published/image-from-ios.jpeg?1674505014=": "assets/images/archive-member-02.jpeg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/published/img-4324.jpeg?1674505497=": "assets/images/archive-member-03.jpeg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/p3190293_orig.jpg": "assets/images/archive-field-01.jpg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/editor/img-20260317-wa0056.jpg?1774467121=": "assets/images/archive-member-04.jpg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/published/me.jpeg?1774643217=": "assets/images/archive-member-05.jpeg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/published/jswanson-gcaecologicalrestoration-fieldshot.jpg?1779556398=": "assets/images/archive-member-06.jpg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/bees-01-sm.jpeg": "assets/images/archive-field-02.jpeg",
    "https://www.ponisiolab.com/uploads/9/4/6/4/94640692/grand-lauren_orig.jpeg": "assets/images/archive-collaborator-lauren-grand.jpeg",
}


def download(url: str, target: Path) -> bool:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.stat().st_size > 0:
        print(f"exists    {target.relative_to(ROOT)}")
        return True
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 PonisioLabMigration/1.0"})
    try:
        with urlopen(req, timeout=40) as r:
            data = r.read()
        target.write_bytes(data)
        print(f"download  {target.relative_to(ROOT)} ({len(data):,} bytes)")
        return True
    except Exception as exc:
        print(f"FAILED    {url}\n          {exc}")
        return False


def rewrite_html(successful):
    for html in ROOT.glob("*.html"):
        text = html.read_text(encoding="utf-8")
        old = text
        for url, rel in successful.items():
            text = text.replace(url, rel)
        if text != old:
            html.write_text(text, encoding="utf-8")
            print(f"rewrite   {html.name}")


def main():
    successful = {}
    for url, rel in ASSETS.items():
        target = ROOT / rel
        if download(url, target):
            successful[url] = rel
        time.sleep(0.15)
    rewrite_html(successful)
    print(f"\nLocalized {len(successful)} of {len(ASSETS)} discovered assets.")
    if len(successful) != len(ASSETS):
        print("Some Weebly assets could not be downloaded. Re-run before cancelling Weebly.")

if __name__ == "__main__":
    main()
