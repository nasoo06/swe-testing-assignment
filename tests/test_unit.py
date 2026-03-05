"""
Unit tests for Quick-Calc core calculation functions.
Each test verifies an individual function in isolation.
"""

import pytest
from calculator import add, subtract, multiply, divide


# --- Basic operation tests ---

def test_add_positive_numbers():
    """Test addition of two positive integers."""
    assert add(5, 3) == 8


def test_subtract_positive_numbers():
    """Test subtraction of two positive integers."""
    assert subtract(10, 4) == 6


def test_multiply_positive_numbers():
    """Test multiplication of two positive integers."""
    assert multiply(6, 7) == 42


def test_divide_positive_numbers():
    """Test division of two positive integers."""
    assert divide(10, 2) == 5.0


# --- Edge case tests ---

def test_divide_by_zero_raises_error():
    """Edge case: division by zero must raise a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_add_negative_numbers():
    """Edge case: addition with negative numbers."""
    assert add(-5, -3) == -8


def test_multiply_by_zero():
    """Edge case: multiplication by zero should return zero."""
    assert multiply(999, 0) == 0


def test_divide_decimal_numbers():
    """Edge case: division with decimal (floating-point) numbers."""
    result = divide(7.5, 2.5)
    assert result == pytest.approx(3.0)


def test_subtract_resulting_negative():
    """Edge case: subtraction resulting in a negative number."""
    assert subtract(3, 10) == -7


def test_multiply_large_numbers():
    """Edge case: multiplication with very large numbers."""
    assert multiply(1_000_000, 1_000_000) == 1_000_000_000_000
