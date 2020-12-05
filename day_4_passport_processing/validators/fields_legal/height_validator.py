import re
from constants import CM_UNIT
from constants import IN_UNIT

class HeightValidator:
    def __init__(self, cm_lower=150, cm_upper=193, in_lower=59, in_upper=76)
        self.__cm_lower = cm_lower
        self.__cm_upper = cm_upper
        self.__in_lower = in_lower
        self.__in_upper = in_upper

    def validate(self, value):
        split = re.split("(cm|in)", value)
        height_value = split[0]
        height_unit = split[1]
        if height_unit == CM_UNIT:
            return float(height_value) >= cm_lower and float(height_value) <= cm_upper 
        elif height_unit == IN_UNIT:
            return float(height_value) >= in_lower and float(height_value) <= in_upper 
