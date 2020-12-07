import pdb
import numpy as np
from helpers.import_data import ImportData

class CheckData:
    def __init__(self, dataset):
        self.dataset = np.array(dataset)
        self.result = []

    def findTwoValuesForTarget(self, target_value):
        result = []
        for data_value in self.dataset:
            target_value_in_array = target_value - data_value
            if self._checkValueInDataset(self.dataset, target_value_in_array):
                result.append(target_value_in_array)
                result.append(data_value)
                break
        return result


    def findThreeValuesForTarget(self, target_value):
        result = []
        for i in self.dataset:
            for j in self.dataset:
                if i == j or i + j >= target_value:
                    continue
                target_value_in_array = target_value - i - j
                if self._checkValueInDataset(self.dataset, target_value_in_array):
                    result.append(target_value_in_array)
                    result.append(i)
                    result.append(j)
                    break
            if len(result) > 0:
                break
        return result


    def _checkValueInDataset(self, dataset, value):
        return np.where(dataset == value)[0].size > 0

class Calculator:
    def calculate(result_set):
        calculate_result = np.prod(result_set)
        print(calculate_result)

if __name__ == "__main__":
    data_file = ImportData("day_1.data", True)
    checker = CheckData(data_file.dataset)
    results = checker.findTwoValuesForTarget(2020)
    Calculator.calculate(results)
    
    results = checker.findThreeValuesForTarget(2020)
    Calculator.calculate(results)
