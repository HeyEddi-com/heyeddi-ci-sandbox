import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "../..");

/**
 * Load shared/config.json from the repo root.
 * @returns {{ app_name: string, version: string, greeting: string }}
 */
export function loadSharedConfig() {
  const raw = readFileSync(join(root, "shared/config.json"), "utf8");
  const data = JSON.parse(raw);
  if (!data.app_name || !data.version) {
    throw new Error("shared config missing required fields");
  }
  return data;
}
