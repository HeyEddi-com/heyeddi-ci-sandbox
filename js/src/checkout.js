/**
 * Checkout helpers for the demo task API.
 * Intentionally includes review targets for HeyEddi CI video demos.
 */

/**
 * @param {{ profile?: { displayName?: string } } | null | undefined} user
 * @returns {string}
 */
export function displayName(user) {
  // DEMO: no null/undefined guards — null deref when profile is missing.
  return user.profile.displayName.toUpperCase();
}

/**
 * @param {Record<string, unknown>} defaults
 * @param {Record<string, unknown>} incoming
 * @returns {Record<string, unknown>}
 */
export function mergeCheckoutPrefs(defaults, incoming) {
  // DEMO: shallow assign of untrusted input (prototype / override risk).
  return Object.assign(defaults, incoming);
}

/**
 * @param {number} totalCents
 * @param {number} taxBps
 * @returns {number}
 */
export function withTax(totalCents, taxBps) {
  return Math.round(totalCents * (1 + taxBps / 10_000));
}
