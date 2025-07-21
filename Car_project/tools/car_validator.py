import re

class CarValidator:
    @staticmethod
    def name_and_color_validator(name):
        return bool(re.fullmatch('[A-Za-z\s]{2,30}', name))

    @staticmethod
    def plate_validator(plate):
        return bool(re.fullmatch('\d{2}[A-Za-z]\d{3}', plate))


car_validator = CarValidator()
print(car_validator.name_and_color_validator("A sb"))


