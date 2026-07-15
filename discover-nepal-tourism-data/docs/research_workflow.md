# Research Workflow

1. Research one district at a time.
2. Add or correct entries in that district Markdown file.
3. Add the same records to the province master CSV and JSON.
4. Add source URLs and verification dates when validating records.
5. Run `python3 scripts/validate_data.py` before committing.
6. Commit small units: one district or one verification batch per commit.

Recommended commit messages:

- `Add first-round tourism inventory for Bagmati/Lalitpur`
- `Verify municipalities for Koshi/Ilam`
- `Add sources and coordinates for Koshi/Jhapa`
