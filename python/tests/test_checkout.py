from sandbox_py.checkout import apply_discount, build_order_query, format_receipt


def test_build_order_query_shape() -> None:
    q = build_order_query("u-1", "paid")
    assert "user_id = 'u-1'" in q
    assert "status = 'paid'" in q


def test_apply_discount_percent() -> None:
    assert apply_discount("total_cents * 9 // 10", 1000) == 900


def test_format_receipt() -> None:
    assert format_receipt("ord_1", 2500) == "order=ord_1 total=$25.00"
