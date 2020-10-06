

"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)
"""


# - The difference between arguments and parameters
def print_name(name):  # name here is the parameter of the function
    pass


print_name('Alex')  # Alex here is the argument of the function


# - Positional and keyword arguments
def foo(a, b, c):
    pass


# both of the following work properly
foo(1, 2, 3)  # positional arguments where order is important
foo(c=3, a=1, b=2)  # keyword arguments where order is no longer important
# we could mix these two together but we could not use a positional argument after a keyword argument


# - Default argument
# just note that default argument must be defined at the end


# - Variable-length arguments (*args and **kwargs)
# args is treated as a tuple and kwargs is treated as a dictionary
def multifoo(a, b, *args, **kwargs):
    for arg in args:
        pass
    for key, value in kwargs.items():
        pass


multifoo(1, 2, 3, 4, 5, 6, six=6, seven=7)


# note that every arguments after the *args must be an keyword argument (i.e. force keyword argument)
def multifoo2(a, b, *args, c, d):  # here c and d must be keyword argument
    pass


# multifoo2(1, 2, 3, 4, 5)  # would raise TypeError (missing c and d)
# multifoo2(1, 2, 3, x=4, y=5)  # would raise TypeError (key must be c and d)


# - Container unpacking into function arguments
def foo_other(a, b, c):
    pass


mylist = [1, 2, 3]  # also works for tuple
foo_other(*mylist)  # use * to unpack arguments from list or tuple (doesn't have to be args)

mydict = {'b': 2, 'c': 3, 'a': 1}
foo_other(**mydict)  # use ** to unpack arguments from dictionary (keys must match the name of parameters)


# - Local vs. global arguments
def foo_another_access():
    x = number  # could access the variable 'number' outside the function (by copying number to x)
    x += 1  # this does not change the variable 'number' outside the function


def foo_another_local():
    number = 5  # this creates a local variable called 'number' instead of changing the 'number' outside the function


def foo_another_global():
    global number  # make the 'number' variable global
    number = 10  # this time the 'number' variable outside the function is changed


number = 123
foo_another_access()
print(number)  # print 123
foo_another_local()
print(number)  # print 123
foo_another_global()
print(number)  # print 10
print()

# if number is mutable object like a list, class etc, then no global is needed for modifying it inside a function


# - Parameter passing (pass by value of reference)
# mutable object could be changed (change value) but not reassigned (change reference) by passing to a function
# immutable object could not be reassigned (value change of immutable object is reassign) by passing to a function
# immutable object within a mutable object could be reassigned (i.e. change value) by passing to a function


def reassign(x):
    # before the line below, x is a parameter (which acts like a local variable)
    x = 5  # this does not change the value of var outside but create a local variable x inside the function instead
    # now x is a local variable (and maybe also a parameter?)


var = 10
reassign(var)  # this would not change the value of var
print(var)  # print 10


def change_mutable(x):
    x.append(5)
    x += [6]  # note the difference between 'x +=' and 'x = x +'


my_list = [1, 2, 3, 4]
change_mutable(my_list)  # this changes my_list
print(my_list)  # print [1, 2, 3, 4, 5, 6]


def reassign_mutable(x):
    x = [1, 2, 3, 4, 5]  # same as immutable object, this creates a local variable x instead of reassign x outside
    x[0] = -100  # this only changes the local variable x

    x = x + [6]  # this line won't change my_list outside either as 'x += [6]' is change but 'x = x + [6]' is reassign


my_list = [1, 2, 3, 4]
reassign_mutable(my_list)  # this does not change my_list
print(my_list)  # print [1, 2, 3, 4]
