import numpy as np
import pdb
from helpers.import_data import ImportData

COUNT_METHOD = 'count'
POSITION_METHOD = 'position'

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

    def checkValidPasswords(self, check_method=COUNT_METHOD):
        count = 0
        for password in self.data:
            bounds = password[0].split("-")
            value_one = int(bounds[0])
            value_two = int(bounds[1])
            letter = password[1]
            password_to_check = password[2]
            if self._check_method(check_method, value_one, value_two, letter, password_to_check):
                count += 1

        return count

    def _check_method(self, check_method, value_one, value_two, letter, password_to_check):
        if check_method == COUNT_METHOD:
            return self._passwordValid(value_one, value_two, letter, password_to_check)
        elif check_method == POSITION_METHOD:
            return self._positionValid(value_one - 1, value_two -1, letter, password_to_check) 

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
    
    def _positionValid(self, first_position, second_position, letter, password):
        return (password[first_position] == letter) ^ (password[second_position] == letter)

if __name__ == "__main__":
    dataFile = ImportData("day_2.data")
    dataSplitter = DataSplitter(dataFile.dataset) 
    split_data = dataSplitter.splitPasswords()
    password_checker = PasswordChecker(split_data)
    count = password_checker.checkValidPasswords()
    print(count)

    count = password_checker.checkValidPasswords('position')
    print(count)
