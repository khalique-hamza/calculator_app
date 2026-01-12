from calculator_program.calculator_history import CalculationResultHistory

history_obj = CalculationResultHistory()
history_obj.load_calculation_history_from_file()
history_obj.preprocess_nested_list()
history_obj.build_history_map()
print(history_obj.calculation_history_map)

print(history_obj.get_last_calculation_history())
print(history_obj.get_n_calculation_history(2))