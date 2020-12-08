from helpers.import_data import ImportData
import re

CONTAIN_SPLIT = "contain"
BAG_SPLIT = ", "

class ParseData:
    def __init__(self, dataset):
        self.dataset = dataset
        self.parsed_results = dict()

    def call(self):
        for line in dataset:
            bag_split = line.split(CONTAIN_SPLIT)
            primary_bag = self.__format_bag(bag_split[0])
            containing_bags = bag_split[1]

    def __format_bag(self, bag_string):
        return re.sub(" (bag|bags)", "", bag_string)

if __name__ == "__main__":
    data_file = ImportData('dataset.data')
    parse_data = ParseData(data_file.dataset)
    parse_data.call()
