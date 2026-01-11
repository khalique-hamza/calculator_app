from calculator_program.calculator import Calculator
from calculator_program.calculator_enum import CalculatorOptionStr
import pytest

@pytest.fixture
def make_calculator():
    def _make_calculator(x, y):
        return Calculator(x, y)
    return _make_calculator

@pytest.fixture
def make_calculator_option_str():
    return CalculatorOptionStr