"""Intentionally smelly auth helper for HeyEddi CI review scoring."""

API_KEY = "sk-live-HARDCODED-SECRET-DO-NOT-SHIP"

def authenticate(token: str) -> bool:
    # Constant-time? No — and compares against a committed secret.
    return token == API_KEY


def run_user_filter(expression: str, payload: dict) -> object:
    # Remote code execution via eval of untrusted input.
    return eval(expression, {}, {"payload": payload})
