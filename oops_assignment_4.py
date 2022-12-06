# --------------------------------------
# Inheritance Assignments (2,3,4,5,6)
# --------------------------------------
#
# 1. Define three classes for each of the following list below (A,B,C,D,E).
# one class must be the superclass and the other two classes being subclasses.
#
# 	A1) Relative (superclass); Sister, Brother, Aunt, Uncle (subclasses)
# 	B2) Parent (superclass); Mom, Dad (subclasses)
# 	C3) Appliance (superclass); Stove, Refrigerator, Oven, Dishwasher (subclasses)
# 	D4) Animal (superclass); Dog, Cat, Hamster, Tiger (subclasses)
# 	E5) Publication (superclass); Book, Magazine, Newspaper (subclasses)

class Relative:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"name: {self.name}, age: {self.age}, gender: {self.gender}"


class Sister(Relative):
    def __init__(self, name, age, gender, unique_char):
        super().__init__(name, age, gender)
        self.unique_char = unique_char

    def get_details(self):
        return super().get_details() + f" unique char : {self.unique_char}"


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_parent_details(self):
        return f"Name: {self.name}, Age: {self.age}"


class Mom(Parent):
    def __init__(self, name, age, parent):
        super().__init__(name, age)
        self.parent = parent

    def get_parent_details(self):
        return super().get_parent_details() + f" parent? {self.parent}"


class Dad(Parent):
    def __init__(self, name, age, drinks):
        super().__init__(name, age)
        self.drinks = drinks

    def get_parent_details(self):
        return super().get_parent_details() + f" drinks {self.drinks}"


p1 = Mom('Aai', 54, "Yes")
print(p1.get_parent_details())

p2 = Dad("baba", 60, "Milk")
print(p2.get_parent_details())
s1 = Sister("Bhagwat", "54", "F", "Dance")

print(s1.get_details())


# C3) Appliance (superclass); Stove, Refrigerator, Oven, Dishwasher (subclasses)
class Appliance:
    def __init__(self, name):
        self.name = name

    def get_app_dets(self):
        return f" Name : {self.name}"


class Dishwasher(Appliance):

    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def get_app_dets(self):
        return super().get_app_dets() + f" Company of appliance {self.company}"
