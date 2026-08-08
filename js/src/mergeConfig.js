/** Intentionally smelly config merge for HeyEddi CI review scoring. */

export function mergeConfig(base, override) {
  // Mutates caller input; no null checks; prototype pollution via __proto__.
  for (const key of Object.keys(override)) {
    base[key] = override[key];
  }
  return base.nested.value.toUpperCase();
}

export function loadUser(users, id) {
  // Crash on missing user — no optional chaining / guards.
  return users.find((u) => u.id === id).email.trim();
}
