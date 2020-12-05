from helpers.import_data import ImportData
import numpy as np
import pdb

BIRTH_YEAR = "byr"
ISSUE_YEAR = "iyr"
EXPIRATION_YEAR = "eyr"
HEIGHT = "hgt"
HAIR_COLOUR = "hcl"
EYR_COLOUR = "ecl"
PASSPORT_ID = "pid"
COUNTRY_ID = "cid"

class PassportReader:
    def __init__(self, dataset):
        self.dataset = dataset
        self.passports = []

    def processPassports(self):
        passport = {}
        for line in self.dataset:
            if len(line) == 0:
                self.passports.append(passport)
                passport = {}
                continue

            passport = self.__processPassportData(line, passport)
        self.passports.append(passport)

    def __processPassportData(self, line, passport):
        split_line = line.split(" ")
        for data_entry in split_line:
            split_key_value = data_entry.split(":")
            passport[split_key_value[0]] = split_key_value[1]
        return passport

class PassportValidator:
    def __init__(self, passports):
        self.passports = passports
        self.__required_keys = [
            BIRTH_YEAR,
            ISSUE_YEAR,
            EXPIRATION_YEAR,
            HEIGHT,
            HAIR_COLOUR,
            EYR_COLOUR,
            PASSPORT_ID
        ]

    def validateCorrectPassports(self):
        correct_passports = 0
        failed = 0
        for passport in self.passports:
            if self.__validPassport(passport):
                correct_passports += 1
            else:
                failed += 1
        return [correct_passports, failed]

    def __validPassport(self, passport):
        passport_keys = passport.keys()
        for required_key in self.__required_keys:
            if required_key in passport_keys:
                continue
            else:
                return False
        return True

if __name__ == "__main__":
    dataFile = ImportData('dataset/day_4.data')
    passportReader = PassportReader(dataFile.dataset)
    passportReader.processPassports()
    print(len(passportReader.passports))
    passportValidator = PassportValidator(passportReader.passports)
    result = passportValidator.validateCorrectPassports()
    print(result)
