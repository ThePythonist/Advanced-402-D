from Models import Human
class Student(Human):
    def __init__(self, name, age, uni, field):
        super().__init__(name, age)
        self.university = uni
        self.field = field

    def entekhab_vahed(self):
        print(f"18 vahed az {self.field}")


ali = Human("Ali", 23)
pooria = Student("Pooria", 24, "Sharif", "Electical Engineering")

# ali.talk()
pooria.entekhab_vahed()
