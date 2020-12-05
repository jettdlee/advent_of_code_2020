import re
class HairColourValidator:
    def validate(self, value):
        return len(re.findall("^#[a-f0-9]{6}$", value)) > 0
