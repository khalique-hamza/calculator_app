class TestCalculator:
    def test_add(self, make_calculator):
        assert make_calculator(x=10, y=2).add() == 12.00

    def test_subtract(self, make_calculator):
        assert make_calculator(x=10, y=2).subtract() == 8.00

    def test_multiply(self, make_calculator):
        assert make_calculator(x=10, y=2).multiply() == 20.00

    def test_divide(self, make_calculator):
        assert make_calculator(x=10, y=2).divide() == 5.00