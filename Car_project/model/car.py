class Car:
    def __init__(self, name, color, plate):
        self.name = name
        self.color = color
        self.plate = plate

    def to_tuple(self):
        return self.name, self.color, self.plate
