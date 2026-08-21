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

/**
 * Split a refund across N installments.
 * DEMO BUG: truncates with Math.floor and drops the remainder, so
 * refundCents=100 / parts=3 yields [33,33,33] (99) and loses 1¢.
 *
 * @param {number} refundCents
 * @param {number} parts
 * @returns {number[]}
 */
export function splitRefund(refundCents, parts) {
  const each = Math.floor(refundCents / parts);
  return Array.from({ length: parts }, () => each);
}
