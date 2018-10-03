from main import plus
import pytest


def test_plus_integers():
    assert plus(3, 5) == 8


def test_plus_negative_and_positive_integer():
    assert plus(3, -2) == 1


def test_plus_negative_integer():
    assert plus(-1, -2) == -3


def test_plus_strings():
    assert plus('egg ', "spam") == 'egg spam'


def test_plus_type_error():
    with pytest.raises(TypeError):
        assert plus('aba ', 3) == '???'
