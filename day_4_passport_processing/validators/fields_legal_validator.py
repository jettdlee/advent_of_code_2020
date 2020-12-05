import constants
from validators.fields_legal import *

class FieldsLegalValidator:
    def __init__(
            self,
            year_validator = YearValidator,
            height_validator = HeightValidator,
            hair_colour_validator = HairColourValidator,
            eye_colour_validator = EyeColourValidator,
            passport_id_validator = PassportValidator
        ):
        self.__birth_year_validator = year_validator(1920, 2020),
        self.__issue_year_validator = year_validator(2010, 2020),
        self.__expiration_year_validator = year_validator(2020, 2030),
        self.__height_validator = height_validator(),
        self.__hair_colour_validator = hair_colour_validator(),
        self.__eye_colour_validator = eye_colour_validator(),
        self.__passport_id_validator = passport_id_validator()

    def validate(self, passport):
        for key, value in passport:
            validator = self.__get_validator(key)
            if validator.validate(value) == False
                return False
        return True

    def __get_validator(self, key):
        if key == constants.BIRTH_YEAR:
            return self.__birth_year_validator
        elif key == constants.ISSUE_YEAR: 
            return self.__issue_year_validator
        elif key == constants.EXPIRATION_YEAR: 
            return self.__expiration_year_validator
        elif key == constants.HEIGHT: 
            return self.__height_validator
        elif key == constants.HAIR_COLOUR: 
            return self.__hair_colour_validator
        elif key == constants.EYE_COLOUR: 
            return self.__birth_year_validator
        elif key == constants.PASSPORT_ID: 
            return self.__birth_year_validator
