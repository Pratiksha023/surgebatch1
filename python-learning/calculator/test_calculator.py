import pytest

from calculator import evaluate


def test_basic():
    assert evaluate("2+3*4") == 14
    assert evaluate("(2+3)*4") == 20
    assert evaluate("10/4") == 2.5
    assert evaluate("2^3") == 8
    assert evaluate("7%3") == 1


def test_float_cleanup():
    assert evaluate("0.1+0.2") == 0.3


def test_errors():
    for bad in ("1/0", "2+", "__import__('os')", "abc"):
        with pytest.raises(ValueError):
            evaluate(bad)
