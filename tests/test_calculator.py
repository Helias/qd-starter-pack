# Test esercizio calculator.py
"""Tests for src/calculator.py."""

from typing import Iterator

import pytest

from src.calculator import (
    add,
    divide,
    format_number,
    main,
    multiply,
    read_number,
    subtract,
)


def fake_input(monkeypatch: pytest.MonkeyPatch, values: list[str]) -> None:
    """Replace input() so that it returns the given values in order."""
    answers: Iterator[str] = iter(values)
    monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))


def test_add() -> None:
    assert add(4, 2) == 6
    assert add(-1, 1) == 0
    assert add(0.5, 0.25) == 0.75


def test_subtract() -> None:
    assert subtract(4, 2) == 2
    assert subtract(2, 4) == -2
    assert subtract(0, 0) == 0


def test_multiply() -> None:
    assert multiply(4, 2) == 8
    assert multiply(-3, 2) == -6
    assert multiply(5, 0) == 0


def test_divide() -> None:
    assert divide(4, 2) == 2
    assert divide(1, 4) == 0.25
    assert divide(-6, 3) == -2


def test_divide_by_zero_returns_none() -> None:
    assert divide(5, 0) is None


def test_format_number() -> None:
    assert format_number(2.0) == "2"
    assert format_number(2.5) == "2.5"
    assert format_number(-3.0) == "-3"


def test_read_number_valid(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_input(monkeypatch, ["4"])
    assert read_number("Insert number: ") == 4


def test_read_number_retries_on_invalid_input(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    fake_input(monkeypatch, ["abc", "", "3.5"])
    assert read_number("Insert number: ") == 3.5
    assert capsys.readouterr().out.count("Invalid number, try again.") == 2


def test_main_example_output(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    fake_input(monkeypatch, ["4", "2"])
    main()
    out = capsys.readouterr().out
    assert "SUM: 6\n" in out
    assert "Difference: 2\n" in out
    assert "Multiplication: 8\n" in out
    assert "Division: 2\n" in out


def test_main_division_by_zero(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    fake_input(monkeypatch, ["5", "0"])
    main()
    out = capsys.readouterr().out
    assert "SUM: 5\n" in out
    assert "Division: impossible (division by zero)" in out
