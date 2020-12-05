from constants import EYE_COLOURS
import re

class EyeColourValidator:
    def validate(self, value):
        return len(re.findall("^(amb|blu|brn|gry|hzl|oth)",value)) > 0

