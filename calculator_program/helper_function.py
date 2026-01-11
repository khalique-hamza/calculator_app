def run_calculation(operation_selection, calculator_obj):
    if operation_selection == "+":
        return calculator_obj.add()
    elif operation_selection == "-":
        return calculator_obj.subtract()
    elif operation_selection == "*":
        return calculator_obj.multiply()
    elif operation_selection == "/":
        return calculator_obj.divide()

