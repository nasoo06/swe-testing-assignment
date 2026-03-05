"""
Integration tests for Quick-Calc.
These tests verify the interaction between the input layer (Calculator class)
and the underlying calculation logic (pure functions).
"""

from calculator import Calculator


def test_full_addition_workflow():
    """
    Integration: Simulate a full user interaction.
    Enter 5, press +, enter 3, press =, and assert the result is 8.
    """
    calc = Calculator()
    calc.enter_number(5)
    calc.set_operator("+")
    calc.enter_number(3)
    result = calc.equals()
    assert result == 8
    assert calc.get_display() == "8"


def test_clear_resets_after_calculation():
    """
    Integration: Verify that pressing Clear after a calculation resets
    the display to 0.
    """
    calc = Calculator()
    calc.enter_number(10)
    calc.set_operator("*")
    calc.enter_number(5)
    calc.equals()
    assert calc.get_display() == "50"

    calc.clear()
    assert calc.get_display() == "0"
    assert calc.result == 0.0


def test_chained_operations():
    """
    Integration: Verify chained operations work correctly.
    5 + 3 = 8, then continue with * 2 = 16.
    """
    calc = Calculator()
    calc.enter_number(5)
    calc.set_operator("+")
    calc.enter_number(3)
    calc.equals()

    calc.set_operator("*")
    calc.enter_number(2)
    result = calc.equals()
    assert result == 16
    assert calc.get_display() == "16"
