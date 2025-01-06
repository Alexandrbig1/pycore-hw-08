from field import Field
import re

class Phone(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise ValueError("Invalid phone format. Use 10 digits.")

    @staticmethod
    def validate(value):
        return bool(re.fullmatch(r"\d{10}", value))