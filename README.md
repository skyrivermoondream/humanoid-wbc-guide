# Humanoid Whole-Body Control: A Topic Map for Graduate Students

English: https://skyrivermoondream.github.io/humanoid-wbc-guide/
中文版：https://skyrivermoondream.github.io/humanoid-wbc-guide/zh/

A one-page guide for graduate students co-supervised with ONE-G:

1. The humanoid whole-body control pipeline in five minutes
2. 13 recent works (SONIC, Any2Any, SuperMimic and more) with videos, plain-language notes and why each matters for inspection
3. Eight needs on an inspection route, matched to abilities, works and topics
4. Six candidate topics with difficulty, reading list and month-one tasks
5. A first-month plan, resources and a glossary

Each language is a single static HTML file with no external fonts or script libraries. Videos are embedded from each paper's official project page, load only when played, and belong to their authors.

## Editing

All text and links live in `src/content.py`. Every string is written as `T("English", "中文")`, so edit both languages together. The illustration is in `src/scene.py`. After editing, run this from the repository root:

```bash
python3 src/build.py
```

It regenerates `index.html` (English, the default) and `zh/index.html` (Chinese). Only Python 3 is needed.

The site is published from the `gh-pages` branch. After committing to `main`, run `git push origin main:gh-pages`, or switch the Pages source to `main` under Settings → Pages.

Compiled by ONE-G (万机). Current as of October 2026.
