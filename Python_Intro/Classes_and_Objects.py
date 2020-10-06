

class Robot:
    def __init__(self, name='Default', color='black', weight=0):  # add '=val' makes a var optional with val being its default value
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):  # self statement is needed, unlike in Java where self is not required
        print("My name is " + self.name)

    def introduce_self2(self):  # self statement is needed even if it has no use
        print("My name is Walala")


r1 = Robot('Tom', 'red', 30)  # r1 = Robot(name='Tom', color='red', weight=30) also works
r1.name = 'Tom'  # this works without defining a constructor and defining name within the Robot class
r1.color = 'red'
r1.weight = 30
r1.introduce_self()
r1.introduce_self2()

# r2 = Robot()  the default constructor is no longer valid if we created a constructor by ourselves
# r2.name = 'Jerry'
# r2.color = 'blue'
# r2.weight = 50
# r2.introduce_self()

r3 = Robot()
r3.introduce_self()
r3 = Robot(color='pink')
print(r3.color)


class Person:
    def __init__(self, name='Default', personality='None', is_sitting=False, robot=None):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting
        self.robot_owned = robot

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


p1 = Person('Daniel', 'extrovert', False, r1)
p2 = Person('Mandy', 'beloved', True)

p1.robot_owned.introduce_self()
p2.robot_owned = r3
p2.robot_owned.introduce_self()
