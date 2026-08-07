from sandbox_py import greet


def test_greet_default() -> None:
    assert greet() == "hello, world"


def test_greet_named() -> None:
    assert greet("eddi") == "hello, eddi"
