from sandbox_py.health import check_health


def test_check_health_ok() -> None:
    result = check_health(version="0.2.0")
    assert result.status == "ok"
    assert result.version == "0.2.0"
    assert "T" in result.checked_at
