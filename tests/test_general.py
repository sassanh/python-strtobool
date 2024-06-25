# ruff: noqa: D100, D101, D102, D103, D104, D107
"""Test the general functions in the project."""

import pytest

from str_to_bool import str_to_bool


def test_one_letter() -> None:
    assert str_to_bool('y')
    assert not str_to_bool('n')


def test_capital_one_letter() -> None:
    assert str_to_bool('Y')
    assert not str_to_bool('N')


def test_yes_no() -> None:
    assert str_to_bool('yes')
    assert not str_to_bool('no')


def test_capital_yes_no() -> None:
    assert str_to_bool('YES')
    assert not str_to_bool('NO')


def test_arbitrary_case() -> None:
    assert str_to_bool('YeS')
    assert not str_to_bool('nO')


def test_true_false() -> None:
    assert str_to_bool('true')
    assert not str_to_bool('false')


def test_capital_true_false() -> None:
    assert str_to_bool('TRUE')
    assert not str_to_bool('FALSE')


def test_arbitrary_case_true_false() -> None:
    assert str_to_bool('TrUe')
    assert not str_to_bool('fAlSe')


def test_on_off() -> None:
    assert str_to_bool('on')
    assert not str_to_bool('off')


def test_capital_on_off() -> None:
    assert str_to_bool('ON')
    assert not str_to_bool('OFF')


def test_arbitrary_case_on_off() -> None:
    assert str_to_bool('oN')
    assert not str_to_bool('oFf')


def test_one_zero() -> None:
    assert str_to_bool('1')
    assert not str_to_bool('0')


def test_invalid() -> None:
    with pytest.raises(ValueError, match='Invalid truth value "foo"'):
        str_to_bool('foo')
    with pytest.raises(ValueError, match='Invalid truth value "2"'):
        str_to_bool('2')
