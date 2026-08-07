/**
 * Convert text to a URL-safe slug.
 * @param {string} input
 * @returns {string}
 */
export function slugify(input) {
  if (typeof input !== "string") {
    throw new TypeError("slugify expects a string");
  }
  return input
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}
