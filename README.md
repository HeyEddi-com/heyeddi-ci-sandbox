# heyeddi-ci-sandbox

Public sandbox for validating [HeyEddi CI](https://ci.heyeddi.com) reviews (LGTM quality) against a small **Python + JavaScript** codebase.

## Layout

| Path | Role |
|------|------|
| `python/` | Tiny Python package (`sandbox_py`) + pytest |
| `js/` | Tiny Node package + node:test |
| `shared/config.json` | Shared config both sides can read |
| `eddi-ci.yaml` | HeyEddi CI policy |

## Local

```bash
# Python
cd python && python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest

# JS
cd js && npm test
```

## Purpose

Open feature PRs stay unmerged so the HeyEddi GitHub App can review them. Not a product.
