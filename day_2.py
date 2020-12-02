import numpy as np
import pdb
from helpers.import_data import ImportData

class DataSplitter:
    def __init__(self, dataset):
        self.dataset = dataset

    def splitPasswords(self):
        result = []
        for line in self.dataset:
            split_line = line.replace(":", "").split(" ")
            result.append(split_line)
        return result
        

class PasswordChecker:
    def __init__(self, data):
        self.data = data

    def checkValidPasswords(self):
        count = 0
        for password in self.data:
            bounds = password[0].split("-")
            lower_bound = int(bounds[0])
            upper_bound = int(bounds[1])
            letter = password[1]
            password_to_check = password[2]
            if self._passwordValid(lower_bound, upper_bound, letter, password_to_check):
                count += 1
        return count

    def _passwordValid(self, lower_bound, upper_bound, letter, password):
        character_count = self._letter_counter(password, letter)
        if character_count >= lower_bound and character_count <= upper_bound:
            return True
        else:
            return False

    def _letter_counter(self, string, char):
        count = 0
        for character in string:
            if char == character:
                count += 1
        return count


if __name__ == "__main__":
    dataFile = ImportData("dataset/day_2.data")
    dataSplitter = DataSplitter(dataFile.dataset) 
    split_data = dataSplitter.splitPasswords()
    password_checker = PasswordChecker(split_data)
    count = password_checker.checkValidPasswords()
    print(count)

