import constants
import re
from validators.fields_legal.year_validator import YearValidator
from validators.fields_legal.height_validator import HeightValidator
from validators.fields_legal.eye_colour_validator import EyeColourValidator
from validators.fields_legal.hair_colour_validator import HairColourValidator
from validators.fields_legal.passport_id_validator import PassportIdValidator
import pdb

class FieldsLegalValidator:
    def __init__(
            self,
            year_validator = YearValidator,
            height_validator = HeightValidator,
            hair_colour_validator = HairColourValidator,
            eye_colour_validator = EyeColourValidator,
            passport_id_validator = PassportIdValidator
        ):
        self.__birth_year_validator = year_validator(1920, 2002)
        self.__issue_year_validator = year_validator(2010, 2020)
        self.__expiration_year_validator = year_validator(2020, 2030)
        self.__height_validator = height_validator()
        self.__hair_colour_validator = hair_colour_validator()
        self.__eye_colour_validator = eye_colour_validator()
        self.__passport_id_validator = passport_id_validator()

    def validate(self, passport):
        for key, value in passport.items():
            if key == constants.COUNTRY_ID:
                continue

            if self.valdate_value(key, value) == False:
                print(f"failed: {key} {value}")
                return False

        return True

    def valdate_value(self, key, value):
        if key == constants.BIRTH_YEAR:
            return int(value) >= 1920 and int(value) <= 2002
        elif key == constants.ISSUE_YEAR: 
            return int(value) >= 2010 and int(value) <= 2020
        elif key == constants.EXPIRATION_YEAR: 
            return int(value) >= 2020 and int(value) <= 2030
        elif key == constants.HEIGHT: 
            return len(re.findall("^((1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in))$", value)) > 0
        elif key == constants.HAIR_COLOUR: 
            return len(re.findall("^#[0-9a-f]{6}$", value)) > 0
        elif key == constants.EYE_COLOUR: 
            return len(re.findall("^(amb|blu|brn|gry|grn|hzl|oth)$", value)) > 0
        elif key == constants.PASSPORT_ID: 
            return len(re.findall("^0[0-9]{8}$", value)) > 0
