class Car:
    def __init__(self, name, model, gb, color):
        self.name = name
        self.model = model
        self.gearbox = gb
        self.color = color

    def park(self):
        print("Parking ...")

    def accelerate(self):
        print(self.name, "Is Accelerating ...")

    def horn(self):
        print("Horn !!!")


dena = Car("Dena", 1402, "Automatic", "Black")
samand = Car("Samand", 1398, "Manual", "White")
