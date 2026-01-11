from calculator_program.calculator import Calculator
import pyinputplus as pyip
import pytest

def setup_tests():
    operation_selection = 1
    x_value = 10
    y_value = 2

    return Calculator(x=x_value, y=y_value)

def test_add():
    calculator_obj = setup_tests()

    assert calculator_obj.add() == 12.00, "Error in add feature"

