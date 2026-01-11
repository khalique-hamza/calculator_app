def run_calculation(operation_selection, calculator_obj):
    operations = {
        "+": calculator_obj.add,
        "-": calculator_obj.subtract,
        "*": calculator_obj.multiply,
        "/": calculator_obj.divide,
    }
    
    # Get the function from the dictionary and call it ()
    action = operations.get(operation_selection)
    
    if action:
        return action()
    return None