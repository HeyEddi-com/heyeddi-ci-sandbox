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

## Related-context fixture

Branch `test/related-context-out-of-diff` renames Python/JS greet exports only.
Callers (`python/tests/test_greet.py`, `js/src/index.js`, JS tests) stay **out of the
diff** so production review can prove related-file packing. `cmd/ping/main.go`
exercises the unsupported-stack note.
