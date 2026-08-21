# Video demo shot list — HeyEddi CI

Repo: [HeyEddi-com/heyeddi-ci-sandbox](https://github.com/HeyEddi-com/heyeddi-ci-sandbox)

## Storyboard

1. **Repo + policy** — show `eddi-ci.yaml`, brief README, green checks on `main`.
2. **Open this PR** — `demo/add-checkout-helpers` (or refresh `/heyeddi review`).
3. **GitHub Checks** — GHA may stay green; HeyEddi Check surfaces findings.
4. **Inline findings** — logic bugs + secret / SQL / null deref / unsafe merge.
5. **Debate** — reply on one thread or `/heyeddi ask …`.
6. **Fix pass** (optional second take) — push a clean commit → LGTM.

## What this PR plants (intentional)

| Area | Issue |
|------|--------|
| Python `free_shipping_eligible` | **Logic bug:** `>` instead of `>=` at the $50 threshold |
| JS `splitRefund` | **Logic bug:** floors and drops remainder cents |
| Python `checkout.py` | Hardcoded service token + SQL f-strings + `eval` |
| JS `checkout.js` | Null deref on nested user + `Object.assign` of untrusted input |

Do not merge this PR into `main` as-is — it is a review target for filming.
