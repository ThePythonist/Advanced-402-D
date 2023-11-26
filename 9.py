import time


class Car:
    def __init__(self, name, model, gb, color, a):  # Paramteres
        # Attributes
        self.name = name
        self.model = model
        self.gearbox = gb
        self.color = color
        self.speed = 0
        self.acceleration = a

    def park(self):
        print("Parking ...")

    def accelerate(self, value):
        print(self.name,"Is accelerating")
        print("Current speed :")
        for i in range(value):
            time.sleep(self.acceleration)
            self.speed += 10
            print(self.speed)

    def horn(self):
        print("Horn !!!")


dena = Car("Dena", 1402, "Automatic", "Black", 1.2)
samand = Car("Samand", 1398, "Manual", "White", 1.6)
persia = Car("Perisa", 1400, "Manual", "Red", 0.8)

persia.accelerate(value=6)
