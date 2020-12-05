from helpers.import_data import ImportData
from helpers.passport_reader import PassportReader
from validators.passport_validator import PassportValidator
import numpy as np
import pdb

if __name__ == "__main__":
    dataFile = ImportData('dataset.data')
    passportReader = PassportReader(dataFile.dataset)
    passportReader.processPassports()
    print(len(passportReader.passports))
    passportValidator = PassportValidator(passportReader.passports)
    result = passportValidator.validateCorrectPassports()
    print(result)
