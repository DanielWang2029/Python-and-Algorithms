

# Function
def hello_func():
    pass


print(hello_func)
print(hello_func())


def another_func():
    return 'This is a Function'


print(another_func().upper())


def input_func(greeting, name='You'):
    return f'{greeting}, {name}\'s Function'


print(input_func('Hi', 'Daniel'))
print(input_func('Hi'))


def student_info(*args, **kwargs):
    """This is a documentation string to explain the functionality of this function."""

    print(args)
    print(kwargs)


# args is list/tuple and kwargs is dictionary
student_info('Math', 'Art', name="John", age=23)
# another way to do this
courses = ['Math', 'Art']
info = {'name': "John", 'age': 23}
student_info(*courses, **info)  # use * and ** to unpack the arguments to args and kwargs

# Advanced functions
# see https://www.python-course.eu/python3_magic_methods.php for functions like '__add__'


# use ': type' to specific which type is expected for the input, but no TypeError would occur if wrong type was used
# if TypeError is wanted for incorrect inputs, use 'isinstance(input, type)' and 'raise typeError'
def magic(x: int) -> int:
    print(x)
    return x + 1


magic(6)
magic(6.0)
