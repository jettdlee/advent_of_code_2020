from helpers.import_data import ImportData
import numpy as np
import pdb
import pandas as pd

class ReadData:
    def __init__(self):
        self.parsed_data = []

    def parse_data(self, dataset):
        group = []
        for line in dataset:
            if len(line) == 0:
                self.parsed_data.append(group)
                group = []
                continue
            data_frame = pd.DataFrame(list(line))
            group.append(data_frame)
        self.parsed_data.append(group)

class CustomChecker:

    def check_answers(self, data):
        group_count = []
        for group in data:
            merged_answer = pd.DataFrame(group[0])
            for answers in group:
                answer_to_merge = pd.DataFrame(answers)
                merged_answer = pd.merge(merged_answer, answer_to_merge) 
            group_count.append(merged_answer.shape[0])
        return group_count


if __name__ == "__main__":
    data_file = ImportData('dataset.data')
    data = ReadData()
    data.parse_data(data_file.dataset)

    checker = CustomChecker()
    result = checker.check_answers(data.parsed_data)
    print(np.sum(result))
