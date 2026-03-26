import importlib

from app.core.config import Settings
from pytest import MonkeyPatch


def test_settings_database_url() -> None:
    settings = Settings(
        DATABASE="mysql+pymysql",
        DATABASE_HOST="localhost",
        DATABASE_PORT=3306,
        DATABASE_USER="user",
        DATABASE_PASSWORD="test_password",  # noqa: S106
        DATABASE_NAME="mydb",
    )

    assert settings.DATABASE_URL == "mysql+pymysql://user:test_password@localhost:3306/mydb"


def test_global_settings_can_be_reloaded_from_env(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE", "mysql+pymysql")
    monkeypatch.setenv("DATABASE_HOST", "127.0.0.1")
    monkeypatch.setenv("DATABASE_PORT", "3307")
    monkeypatch.setenv("DATABASE_USER", "tester")
    monkeypatch.setenv("DATABASE_PASSWORD", "test_password")
    monkeypatch.setenv("DATABASE_NAME", "ripple")

    import app.core.config as config_module

    reloaded = importlib.reload(config_module)

    reloaded.get_settings.cache_clear()
    settings = reloaded.get_settings()

    assert settings.DATABASE == "mysql+pymysql"
    assert settings.DATABASE_HOST == "127.0.0.1"
    assert settings.DATABASE_PORT == 3307
    assert settings.DATABASE_USER == "tester"
    assert settings.DATABASE_PASSWORD == "test_password"  # noqa: S105
    assert settings.DATABASE_NAME == "ripple"
    assert settings.DATABASE_URL == "mysql+pymysql://tester:test_password@127.0.0.1:3307/ripple"
