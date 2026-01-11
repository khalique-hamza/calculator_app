from calculator_program.calculator import Calculator
import pyinputplus as pyip

def run_calculation(operation_selection, calculator_obj):
    if operation_selection == 1:
        return calculator_obj.add()

def main():
    print("Calculator Program Booted:\n")
    print("*Please note calculator only works for 2 numbers.")
    
    calculator_options = [1]

    while True:
        operation_selection = pyip.inputInt("Please select operation: (1) Add\n")
    
        if operation_selection not in calculator_options:
            print("Incorrect operation selection. Please try again.\n")
        else:
            break
        
    x_value = pyip.inputFloat("Please enter the first number:\n")
    y_value = pyip.inputFloat("Please enter the second number:\n")

    calculator_obj = Calculator(x=x_value, y=y_value)

    result = run_calculation(operation_selection=operation_selection, calculator_obj=calculator_obj)

    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
