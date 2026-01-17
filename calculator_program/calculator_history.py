import csv
from dataclasses import dataclass
from calculator_program.errors import NegativeError
import os

@dataclass
class CalculationResult:
    num_1: float
    num_2: float
    operation: str
    result: float

    @classmethod
    def create_calculation_result(cls, id, calculation_row):
        num_1, num_2, operation, result = calculation_row[0], calculation_row[2], calculation_row[1], calculation_row[4]

        return cls(
            num_1=num_1,
            num_2=num_2,
            operation=operation,
            result=result
        )


class CalculationResultHistory:
    def __init__(self):
        self.calculation_history_file_path = os.path.join(os.getcwd(), "calculator_program", "calculation_history", "calculation_history.txt")
        self.calculation_history_list = []
        self.calculation_history_map = {}


    def get_calculation_history_file_path(self):
        return self.calculation_history_file_path
    
    
    def get_calculation_history_list(self):
        return self.calculation_history_list
    

    def get_calculation_history_map(self):
        return self.calculation_history_map


    def parse_calculation_result(self, calculation_result_record):
        return f"{calculation_result_record.num_1} {calculation_result_record.operation} {calculation_result_record.num_2} = {calculation_result_record.result}"

    def get_nth_calculation_history(self, n):
        if n < 0:
            raise NegativeError("Negative Error: Index position cannot be negative.")
        
        if n in self.calculation_history_map.keys():
            return self.parse_calculation_result(self.calculation_history_map[n])
        else:
            raise ValueError("Invalid index: Value not found in map.")
        
    def get_all_calculation_history(self):
        calculation_history_map = self.get_calculation_history_map()
        if not calculation_history_map:
            return "No history found."
        elif len(calculation_history_map) == 0:
            return self.get_last_calculation_history()
        for calculation_history_idx in calculation_history_map.keys():
            print(self.get_nth_calculation_history(calculation_history_idx))
            

    def get_last_calculation_history(self):
        calculation_history_map = self.get_calculation_history_map()
        if not calculation_history_map:
            return "No history found."
        return self.parse_calculation_result(calculation_history_map[0])

    def build_history_map(self):
        for idx, calculation in enumerate(self.calculation_history_list):
            calculation_row = calculation.split(" ")
            self.calculation_history_map[idx] = CalculationResult.create_calculation_result(id=idx, calculation_row=calculation_row)


    def preprocess_nested_list(self):
        self.calculation_history_list = [calculation[0] for calculation in self.calculation_history_list][::-1]


    ### File related functions
    def load_calculation_history_from_file(self):
        try:
            with open(self.calculation_history_file_path, mode="r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    self.calculation_history_list.append(row)
        except FileNotFoundError:
            print("File not found.")


    def write_history_to_file():
        pass

