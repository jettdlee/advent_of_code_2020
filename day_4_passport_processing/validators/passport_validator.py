from validators.fields_present_validator import FieldsPresentValidator
from validators.fields_legal_validator import FieldsLegalValidator

class PassportValidator:
    def __init__(
            self,
            passports,
            fields_present_validator = FieldsPresentValidator,
            fields_legal_validator = FieldsLegalValidator
        ):
        self.passports = passports
        self.__fieldsPresentValidator = fields_present_validator()
        self.__fieldsLegalValidator = fields_legal_validator()

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
        return self.__fieldsPresentValidator.validate(passport) and self.__fieldsLegalValidator.validate(passport)
