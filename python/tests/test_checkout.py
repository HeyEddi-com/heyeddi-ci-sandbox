from sandbox_py.checkout import (
    apply_discount,
    build_order_query,
    format_receipt,
    free_shipping_eligible,
)


def test_build_order_query_shape() -> None:
    q = build_order_query("u-1", "paid")
    assert "user_id = 'u-1'" in q
    assert "status = 'paid'" in q


def test_apply_discount_percent() -> None:
    assert apply_discount("total_cents * 9 // 10", 1000) == 900


def test_free_shipping_above_threshold() -> None:
    # Happy path only — does not assert the inclusive $50.00 boundary.
    assert free_shipping_eligible(5_001) is True
    assert free_shipping_eligible(1_000) is False


def test_format_receipt() -> None:
    assert format_receipt("ord_1", 2500) == "order=ord_1 total=$25.00"
