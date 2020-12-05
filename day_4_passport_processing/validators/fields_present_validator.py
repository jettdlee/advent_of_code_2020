import constants

class FieldsPresentValidator:
    def __init__(
            self,
            required_keys = [constants.BIRTH_YEAR, constants.ISSUE_YEAR, constants.EXPIRATION_YEAR,
                constants.HEIGHT, constants.HAIR_COLOUR, constants.EYE_COLOUR, constants.PASSPORT_ID]
        ):

        self.__required_keys = required_keys

    def validate(self, passport):
        passport_keys = passport.keys()
        for required_key in self.__required_keys:
            if required_key in passport_keys:
                continue
            else:
                return False
        return True
