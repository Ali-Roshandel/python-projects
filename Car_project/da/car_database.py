class CarDa:
    def __init__(self,name):
        self.name = name
    def save(self):
        print(f"Car {self.name} Information Saved")

    def edit(self):
        print(f"Car {self.name} Information Edited")

    def remove(self):
        print(f"Car {self.name} Information Removed")
