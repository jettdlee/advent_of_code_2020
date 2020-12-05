from validators.fields_present_validator import FieldsPresentValidator
from validators.fields_legal_validator import FieldsLegalValidator

class PassportValidator:
    def __init__(
            self,
            fields_present_validator = FieldsPresentValidator,
            fields_legal_validator = FieldsLegalValidator
        ):
        self.__fieldsPresentValidator = fields_present_validator()
        self.__fieldsLegalValidator = fields_legal_validator()

    def validateFieldsPresentPassports(self, passports):
        correct_passports = []
        for passport in passports:
            if self.__fieldsPresentValidator.validate(passport):
                correct_passports.append(passport)
        return correct_passports

    def validateFieldsCorrectPassports(self, passports):
        correct_passports = []
        for passport in passports:
            if self.__fieldsLegalValidator.validate(passport):
                correct_passports.append(passport)
        return correct_passports
