import assert from "node:assert/strict";
import { test } from "node:test";
import { greet } from "../src/greet.js";

test("greet default", () => {
  assert.equal(greet(), "hello, world");
});

test("greet named", () => {
  assert.equal(greet("eddi"), "hello, eddi");
});
