class CarDa:
    def __init__(self, car):
        self.car = car
    def save(self):
        print(f"Car {self.car} Saved")

    def edit(self):
        print(f"Car {self.car} Edited")

    def remove(self):
        print(f"Car {self.car} Removed")
