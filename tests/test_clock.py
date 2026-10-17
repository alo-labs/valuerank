from datetime import datetime, timedelta, timezone

import pytest

from valuerank import clock


def test_utcnow_defaults_to_the_current_utc_time(monkeypatch):
    monkeypatch.delenv(clock.ENV_VAR, raising=False)

    moment = clock.utcnow()

    assert moment.tzinfo == timezone.utc
    assert abs(datetime.now(timezone.utc) - moment) < timedelta(seconds=5)


def test_utcnow_honours_pinned_instant_with_z_suffix(monkeypatch):
    monkeypatch.setenv(clock.ENV_VAR, "2026-10-07T17:23:20Z")

    assert clock.utcnow() == datetime(2026, 10, 7, 17, 23, 20, tzinfo=timezone.utc)


def test_utcnow_normalises_offsets_and_naive_values_to_utc(monkeypatch):
    monkeypatch.setenv(clock.ENV_VAR, "2026-10-07T19:23:20+02:00")
    assert clock.utcnow() == datetime(2026, 10, 7, 17, 23, 20, tzinfo=timezone.utc)

    monkeypatch.setenv(clock.ENV_VAR, "2026-10-07T17:23:20")
    assert clock.utcnow() == datetime(2026, 10, 7, 17, 23, 20, tzinfo=timezone.utc)


def test_blank_override_falls_back_to_the_current_time(monkeypatch):
    monkeypatch.setenv(clock.ENV_VAR, "   ")

    assert abs(datetime.now(timezone.utc) - clock.utcnow()) < timedelta(seconds=5)


def test_invalid_override_raises_a_clear_error(monkeypatch):
    monkeypatch.setenv(clock.ENV_VAR, "yesterday")

    with pytest.raises(ValueError, match="VALUERANK_NOW must be an ISO 8601 instant"):
        clock.utcnow()


def test_iso_z_formats_whole_seconds_with_z_suffix(monkeypatch):
    monkeypatch.setenv(clock.ENV_VAR, "2026-10-07T17:23:20.654321Z")

    assert clock.iso_z() == "2026-10-07T17:23:20Z"
    assert clock.iso_z(datetime(2026, 1, 2, 3, 4, 5, 999, tzinfo=timezone.utc)) == "2026-01-02T03:04:05Z"
