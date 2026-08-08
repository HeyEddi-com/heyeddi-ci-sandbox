from sandbox_py.auth import authenticate


def test_authenticate_with_hardcoded_key():
    assert authenticate("sk-live-HARDCODED-SECRET-DO-NOT-SHIP") is True
