import assert from "node:assert/strict";
import { test } from "node:test";
import { loadSharedConfig } from "../src/config.js";

test("loadSharedConfig returns app_name", () => {
  const cfg = loadSharedConfig();
  assert.equal(cfg.app_name, "heyeddi-ci-sandbox");
  assert.ok(cfg.version);
});
