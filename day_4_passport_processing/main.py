from helpers.import_data import ImportData
from helpers.passport_reader import PassportReader
from validators.passport_validator import PassportValidator
import numpy as np
import pdb

if __name__ == "__main__":
    dataFile = ImportData('dataset.data')
    passportReader = PassportReader(dataFile.dataset)
    passportReader.processPassports()

    passportValidator = PassportValidator()
    passports_with_all_fields_present = passportValidator.validateFieldsPresentPassports(passportReader.passports)
    print(len(passports_with_all_fields_present))
    passports_with_all_fields_legal = passportValidator.validateFieldsCorrectPassports(passports_with_all_fields_present)
    print(len(passports_with_all_fields_legal))
