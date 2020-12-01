import pdb
import numpy as np

class ImportData:
    def __init__(self, fileName):
        with open(fileName, 'r') as f:
            self.dataset = []
            for line in f:
                result = self.__convertLine(line)
                self.dataset.append(result)
    
    def __convertLine(self, line):
        result = line
        result = result.strip('\n')
        result = int(result)
        return result

class CheckData:
    def __init__(self, dataset):
        self.dataset = np.array(dataset)
        self.result = []

    def findTarget(self, target_value):
        result = []
        for data_value in self.dataset:
            target_value_in_array = target_value - data_value
            if self._checkValueInDataset(self.dataset, target_value_in_array):
                result.append(target_value_in_array)

        calculate_result = result[0] * result[1]
        print(f'values found, {result[0]} * {result[1]} = {calculate_result}')

    def findCubeTarget(self, target_value):
        result = []

    def _checkValueInDataset(self, dataset, value):
        return np.where(dataset == value)[0].size > 0


if __name__ == "__main__":

    data_file = ImportData("day_1.data")
    checker = CheckData(data_file.dataset)
    checker.findTarget(2020)
    
