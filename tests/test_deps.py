import contextlib
from typing import Any

from app.api.deps import get_db
from pytest import MonkeyPatch


class DummySession:
    def __init__(self) -> None:
        self.closed = False

    def close(self) -> None:
        self.closed = True


def test_get_db_yields_session_and_closes(monkeypatch: MonkeyPatch) -> None:
    dummy_session = DummySession()

    def fake_session_local() -> Any:
        return lambda: dummy_session

    monkeypatch.setattr("app.api.deps.get_session_local", fake_session_local)

    generator = get_db()
    db = next(generator)

    assert db is dummy_session

    with contextlib.suppress(StopIteration):
        next(generator)

    assert dummy_session.closed is True
