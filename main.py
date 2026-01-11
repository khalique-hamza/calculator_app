from calculator_program.calculator import Calculator
from calculator_program.calculator_enum import CalculatorOptionStr
from calculator_program.helper_function import run_calculation
import pyinputplus as pyip

def main():
    print("Calculator Program Booted:\n")
    print("*Please note calculator only works for 2 numbers.\n")

    operation_selection_menu = """Please select operation: +, -, *,/:\n"""

    while True:
        operation_selection = pyip.inputChoice(prompt=operation_selection_menu, choices=["+", "-", "*", "/"])

        if any(operation_selection == operation.value for operation in CalculatorOptionStr):
            break
        else:
            print("Incorrect operation selection. Please try again.\n")
        
    x_value = pyip.inputFloat("Please enter the first number:\n")
    y_value = pyip.inputFloat("Please enter the second number:\n")

    calculator_obj = Calculator(x=x_value, y=y_value)

    result = run_calculation(operation_selection=operation_selection, calculator_obj=calculator_obj)

    print(f"{x_value} {operation_selection} {y_value} = {result}")

if __name__ == "__main__":
    main()
