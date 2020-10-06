

# decorator is a package wrapped outside a function
# we use @decorator-function before the definition of a function to declare decorator
# decorator function must take a func as the only input and return a replacement func

# default decorator is function decorator, i.e. use decorator function

# common usage/purposes of decorator: time, debug, check, update etc.


import functools


# (function) decorator template
def my_decorator(func):  # take a function as input

    @functools.wraps(func)  # make sure that wrapper has the same name and info as func
    def wrapper(*args, **kwargs):  # define another function that do something before and after func
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper  # return the defined function


# an example
def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result

    return wrapper


@start_end_decorator  # this is the same as 'print_name = start_end_decorator(print_name)', note that no () is added
def print_name():
    print('Alex')


# print_name = start_end_decorator(print_name)  # change the function to the modified/returned function

print_name()  # print start, alex and end


@start_end_decorator
def add5(x):
    return x + 5


print(add5(24))  # print start and end while executing add5, then print the result 29
print()

print(help(add5))  # if functools are not used, print info for wrapper instead of add5
print(add5.__name__)  # if functools are not used, print wrapper instead of add5
print()


def repeat(num_times):  # this layer is needed because we have input num_times

    def decorator_repeat(func):  # this is the actual decorator which have a function as input

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):  # implement the repeat functionality
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator_repeat  # return the actual decorator (decorator_repeat)


@repeat(num_times=3)  # note that normally there isn't (), this is because the decorator is the returned func of repeat
def greet(name):
    print(f'Hello {name}')


greet('Alex')  # print Alex 3 times
print()


def debug(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]  # {sth!r} in f string is the same as {repr(sth)}
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result

    return wrapper


@debug  # multiple decorator could be applied
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


say_hello('Alex')
print()


# example of a class decorator
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):  # make the class instance callable
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        # In general, could add any functionality above
        return self.func(*args, **kwargs)


@CountCalls  # since CountCalls could be called, itself become the (class) decorator
def say_hello_class():
    print('Hello')


# The above process of class decorator is different than function decorator:
# First, we need to understand what @CountCalls represent
# here @CountCalls equals to 'say_hello_class = CountCalls(say_hello_class)'
# which means say_hello_class is actually an instance of the CountCalls class with self.func = say_hello_class
# Then, we we call say_hello_class by invoking the __call__ function of the CountCalls class
# this execute some functionality added in __call__ function and finally invoke self.func, which is say_hello_class
# note that the passed/input arguments for __call__ function is the same as say_hello_class
# Finally, by executing __call__ function, we executed say_hello_class and return its result

say_hello_class()
say_hello_class()
