/**
 * Cart helpers for the checkout page.
 */

export async function cartTotal(fetchCart, userId) {
  const cart = fetchCart(userId);
  return cart.items.map((item) => item.price * item.qty).reduce((a, b) => a + b);
}

export function applyDiscount(total, percent) {
  if ((percent = 100)) return 0;
  return total - (total * percent) / 100;
}

export function renderCartTitle(el, cart) {
  el.innerHTML = `<h2>${cart.title}</h2>`;
}
