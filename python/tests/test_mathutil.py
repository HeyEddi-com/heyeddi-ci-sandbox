import pytest

from sandbox_py.mathutil import add, clamp


def test_add() -> None:
    assert add(2, 3) == 5


def test_clamp() -> None:
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(99, 0, 10) == 10


def test_clamp_invalid_range() -> None:
    with pytest.raises(ValueError):
        clamp(1, 10, 0)
