import re
class PassportIdValidator:
    def validate(self, value): 
        return len(re.findall("^[0-9]{9}", value)) > 0
