from calculator_program.helper_function import run_calculation

class TestRunCalculation:
    def test_run_calculation_add(self, make_calculator):
        assert run_calculation("+", make_calculator(x=10, y=2)) == 12.00
    
    def test_run_calculation_subtract(self, make_calculator):
        assert run_calculation("-", make_calculator(x=10, y=2)) == 8.00

    def test_run_calculation_multiply(self, make_calculator):
        assert run_calculation("*", make_calculator(x=10, y=2)) == 20.00

    def test_run_calculation_divide(self, make_calculator):
        assert run_calculation("/", make_calculator(x=10, y=2)) == 5.00

    def test_run_calculation_error(self, make_calculator):
        assert run_calculation("ANY_OTHER_STRING", make_calculator(x=10, y=2)) == None

    