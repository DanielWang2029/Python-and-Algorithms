

import copy


# example of change of reference
val = 5
cpy = val  # create a new reference to the same object
cpy = 6  # make cpy a reference to a new object, which doesn't affect val
print(val, cpy)  # print 5, 6

mylist = [0, 1, 2, 3, 4]
cpy = mylist  # create a new reference to the same object (instead of copy the object)
cpy[0] = -1  # change the list object, which affect both mylist and cpy
print(mylist, cpy)  # print [-1, 1, 2, 3, 4], [-1, 1, 2, 3, 4]
print()


# example of copy
# - shallow copy: one level deep, only references of nested child objects
# - deep copy: full independent copy
mylist = [0, 1, 2, 3, 4]
cpy = copy.copy(mylist)  # create a new reference to the shallow copy of mylist
cpy = mylist[:]  # this is also a shallow copy
cpy[0] = -1  # change the shallow copy, which doesn't affect mylist
print(mylist, cpy)  # print [0, 1, 2, 3, 4], [-1, 1, 2, 3, 4]

mylist = [[0, 1], [2, 3], [4, 5]]
cpy = copy.copy(mylist)
cpy[0][0] = -1  # since mylist is nested and cpy is a shallow copy, this would affect both mylist and cpy
print(mylist, cpy)  # print [[-1, 1], [2, 3], [4, 5]], [[-1, 1], [2, 3], [4, 5]]

mylist = [[0, 1], [2, 3], [4, 5]]
cpy = copy.deepcopy(mylist)  # create a new reference to the deep copy of mylist
cpy[0][0] = -1  # this would only affect cpy since it's a deep copy of mylist and everything in cpy is independent
print(mylist, cpy)  # print [[0, 1], [2, 3], [4, 5]], [[-1, 1], [2, 3], [4, 5]]
print()


# copy of customized object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Alex', 27)
p2 = p1
p2.age = 28  # this would affect both p1 and p2
print(p1.age, p2.age)  # print 28, 28

p1 = Person('Alex', 27)
p2 = copy.copy(p1)
p2.age = 28  # this only affect p2
print(p1.age, p2.age)  # print 27, 28
print()


# copy of nested customized object
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Alex', 55)
p2 = Person('Peter', 23)
company1 = Company(p1, p2)
company2 = copy.copy(company1)
company2.boss.age = 56  # since company2 is a shallow copy and age is at level 2, this would affect both companies
print(company1.boss.age, company2.boss.age)  # print 56, 56

p1 = Person('Alex', 55)
p2 = Person('Peter', 23)
company1 = Company(p1, p2)
company2 = copy.deepcopy(company1)
company2.boss.age = 56  # this would only affect company2
print(company1.boss.age, company2.boss.age)  # print 55, 56
