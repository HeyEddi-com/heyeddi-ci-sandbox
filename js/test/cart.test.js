import assert from "node:assert/strict";
import { test } from "node:test";
import { cartTotal } from "../src/cart.js";

test("cartTotal sums items", async () => {
  const fetchCart = () => ({ items: [{ price: 5, qty: 2 }, { price: 3, qty: 1 }] });
  assert.equal(await cartTotal(fetchCart, "u1"), 13);
});
