/** @param {string} [name] */
export function greetUser(name = "world") {
  // Renamed from greet — js/src/index.js and tests still import { greet }.
  return `hello, ${name}`;
}
