import assert from "node:assert/strict";
import { test } from "node:test";
import { formatDate } from "../src/formatDate.js";

test("formatDate ISO", () => {
  assert.equal(formatDate("2026-08-07T12:00:00Z"), "2026-08-07");
});

test("formatDate rejects invalid", () => {
  assert.throws(() => formatDate("not-a-date"), TypeError);
});
