"""
    "ENCAPSULATION"
class team ():

    def __init__(self, Captain, Wicketkeeper):
        self.Captain = Captain
        self.Wicketkeeper = Wicketkeeper

    def start_match(self):
        print("Match started.")
my_team = team("ROHIT SHARMA","KL RAHUL")
print(my_team.Wicketkeepero)
my_team.start_match()


class Bike:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def start_engine(self):
        print("Engine started.")
my_Bike = Bike("KTM", "RC100")
print(my_Bike.brand)
print(my_Bike.model)
my_Bike.start_engine()


     "POLYMORPHISM"
class India():
    def captain(self):
        print("Rohit Sharma is captain of Indian Cricket Team")
    def king(self):
        print("Virat Kohli is a King of Indian Cricket Team ")
    def yorker(self):
        print("Bumrah is yorker king of Indian Cricket Team")

class Australia ():
    def captain(self):
        print(" \n  Pat Cummins is captain of Kangaroo's Cricket Team")

    def king(self):
        print("Maxwell is a King of Kangaroo's Cricket Team ")

    def yorker(self):
        print("Starc is yorker king of Kangaroo's Cricket Team")

obj_ind = India( )
obj_aus = Australia( )

for cricket in (obj_ind, obj_aus):
    cricket.captain()
    cricket.king()
    cricket.yorker()


   "ABSTRACTION"
"from abc import ABCMeta, abstractmethod"
from abc import ABC, abstractmethod
class Shape (ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle:
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth =7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

"SINGLE INHERITANCE"
class ParentClass:
    def par_func(self):
        print("Rohit Shrama is my Idol")

# Child class
class ChildClass(ParentClass):
    def child_func(self):
        print("Rohit Saraf is my Fav Actor")

# Driver code
obj1 = ChildClass()
obj1.par_func()
obj1.child_func()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The Name of Employee :{self.id} is {self.name}")

class Programmer (Employee):
    def showLanguage(self):
        print("The default language is Python")

e1 = Employee("MANASI", 420)
e1.showDetails()
e2 = Programmer("ROHIT", 421)
e2.showDetails()
e2.showLanguage()
"""
"SINGLE INHERITANCE "
"""class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def info(self):
        print(f"The name of Animal is {self.name} and its species is  {self.species}")

    def make_sound(self):
        print("The sound of the animal")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species = "Cat")
        self.breed = breed

    def make_sound(self):
        print("MEOW MEOW")

d = Cat("Bombay Cat","Fuzzy")
d.info()
d.make_sound()

a = Animal("Fuzzy","Bombay Cat")
a.make_sound()
"""

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def show_Details(self):
        print(f"Name : {self.name}")
        print(f"Species: {self.species}")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species = "Cat")
        self.breed = breed

    def show_details(self):
        Animal.show_Details(self)
        print(f"Breed: {self.breed}")

class PersianCat(Cat):
    def __init__(self, name, color):
        Cat.__init__(self, name, breed ="PersianCat")
        self.color = color

    def show_details(self):
         Cat.show_details(self)
         print(f"Color: {self.color}")

o =  PersianCat("Bella", "GREY ")
o.show_details()
print(PersianCat.mro())