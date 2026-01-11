class TestCalculatorOptionStr:
    def test_add(self, make_calculator_option_str):
        assert make_calculator_option_str.ADD.value == "+"

    def test_subtract(self, make_calculator_option_str):
        assert make_calculator_option_str.SUBTRACT.value == "-"

    def test_multiply(self, make_calculator_option_str):
        assert make_calculator_option_str.MULTIPLY.value == "*"

    def test_divide(self, make_calculator_option_str):
        assert make_calculator_option_str.DIVIDE.value == "/"