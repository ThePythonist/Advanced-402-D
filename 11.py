from math import pi


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print((self.length + self.width) * 2)


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        print(str(self.radius ** 2 * pi))

    def perimeter(self):
        print(self.radius * 2 * pi)


while True:
    shape = input("""
    1 ==> Rectangle
    2 ==> Circle
    Choose : """)

    if shape == "1":
        l = float(input("Enter length : "))
        w = float(input("Enter width : "))
        rec = Rectangle(l, w)
        print("Area : ", end="")
        rec.area()
        print("Perimeter : ", end="")
        rec.perimeter()
        # break
    elif shape == "2":
        r = float(input("Enter radius : "))
        cir = Circle(r)
        print("Area : ", end="")
        cir.area()
        print("Perimeter : ", end="")
        cir.perimeter()
        # break
    else:
        print("Wrong option. Try again")
