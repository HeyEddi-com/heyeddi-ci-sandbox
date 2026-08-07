from sandbox_py.config import load_shared_config


def test_load_shared_config() -> None:
    cfg = load_shared_config()
    assert cfg["app_name"] == "heyeddi-ci-sandbox"
    assert cfg["version"]
    assert cfg["greeting"]
