from model.car import *
from tools.car_validator import *
from da.car_database import *


class CarController:
    def save(self, name, color, plate):
        try:
            if text_validator(name) and text_validator(color) and plate_validator(plate):
                car = Car(name, color, plate)
                car_da = CarDa(car)
                car_da.save()
                return True, "Car Saved Successfully"
            else:
                raise ValueError("Invalid Input")
        except Exception as e:
            return False, str(e)