

class Dog(object):  # Dog is an inheritance of object
    dogs = []  # this is a class(static) variable

    def __init__(self, name, age):
        self.name = name  # this is an attribute
        self.age = age
        self.dogs.append(self)

    def speak(self):  # this is a method
        print(f"Hi, I am {self.name}, {self.age} years old")

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

    def talk(self):
        print('Bark!')

    @classmethod  # this kind of method could be called using the class name without an instance
    def num_dogs(cls):  # cls stands for the class, representing the name of the class
        return len(cls.dogs)

    @staticmethod  # static method are like a function within a class, they have no access to any other material
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("Bark!")
        # print(dogs)  Note that this wouldn't work because static method have no access to class(static) variables


tim = Dog('Tim', 5)
fred = Dog('Fred', 7)
# the difference between an method and a function is that methods are called on an object but functions are not
tim.speak()
fred.speak()
tim.change_age(10)
print(tim.name, tim.age)
tim.add_weight(50)
print(tim.weight)

print(Dog.dogs)  # static variables could be called by the class name
print(tim.dogs)  # this also works
print(Dog.num_dogs())  # calling a class method using the class name
print(tim.num_dogs())  # this also works
Dog.bark(3)
tim.bark(3)


class Cat(Dog):  # Cat is an inheritance of Dog
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def talk(self):
        print('Meow!')

    def override_name(self, name):
        self.name = name


sam = Cat('Sam', 8, 'blue')
sam.speak()
sam.talk()
sam.override_name('wtf')
sam.speak()


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def length(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __len__(self):
        import math
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __eq__(self, other):
        return self.x ** 2 + self.y ** 2 == other.x ** 2 + other.y ** 2

    def __str__(self):  # str function convert a object into a string which makes it printable
        return f'({self.x}, {self.y})'


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3

print(p5, p6, p7)
print(p1 == p2)
print(p1 > p2)
print(p4 <= p3)
print(len(p1))

# import Python_Intro.To_Be_Imported_by_COA
# test = Python_Intro.To_Be_Imported_by_COA.NotPrivate('Daniel')
# the above code also works but it's to long and complicated
from Python_Intro.To_Be_Imported_by_COA import NotPrivate  # here '.' has the same function as '/' in directory
test = NotPrivate('Daniel')  # by using from xxx import, we don't have to add xxx. in front of the function name
test._display()  # though this works, don't do this as _display function as meant to be private
test.display()

import os
print(os.getcwd())  # print Python_Fundamentals/Python_Intro as the current working directory
