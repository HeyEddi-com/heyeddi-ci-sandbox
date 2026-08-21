import assert from "node:assert/strict";
import { test } from "node:test";
import {
  displayName,
  mergeCheckoutPrefs,
  splitRefund,
  withTax,
} from "../src/checkout.js";

test("displayName uppercases", () => {
  assert.equal(
    displayName({ profile: { displayName: "eddi" } }),
    "EDDI",
  );
});

test("mergeCheckoutPrefs overlays keys", () => {
  const base = { currency: "USD", tip: 0 };
  const out = mergeCheckoutPrefs(base, { tip: 15 });
  assert.equal(out.tip, 15);
  assert.equal(out.currency, "USD");
});

test("withTax adds basis points", () => {
  assert.equal(withTax(1000, 825), 1083);
});

test("splitRefund even split", () => {
  // Happy path only — does not assert remainder cents are preserved.
  assert.deepEqual(splitRefund(99, 3), [33, 33, 33]);
});
