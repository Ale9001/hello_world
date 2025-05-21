import pytest
from src.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 5, 5)
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 7, -7),
    (-3, -6, 3)
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (4, 3, 12),
    (-2, 5, -10),
    (0, 99, 0)
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


def test_divide(calc):
    assert calc.divide(10, 2) == 5


def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.divide(10, 0)


def test_power(calc):
    assert calc.power(2, 3) == 8


@pytest.mark.parametrize("x,expected", [
    (4, 2),
    (9, 3),
    (0, 0)
])
def test_sqrt(calc, x, expected):
    assert calc.sqrt(x) == expected


def test_sqrt_negative(calc):
    with pytest.raises(ValueError, match="Cannot take square root of a negative number"):
        calc.sqrt(-16)