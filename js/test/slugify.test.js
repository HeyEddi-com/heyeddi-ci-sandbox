import assert from "node:assert/strict";
import { test } from "node:test";
import { slugify } from "../src/slugify.js";

test("slugify basic", () => {
  assert.equal(slugify("Hello World"), "hello-world");
});

test("slugify trims punctuation", () => {
  assert.equal(slugify("  Hey Eddi!! "), "hey-eddi");
});

test("slugify rejects non-strings", () => {
  assert.throws(() => slugify(42), TypeError);
});
