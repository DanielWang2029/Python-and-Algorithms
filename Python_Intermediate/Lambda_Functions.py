

# lambda x, y, ...: expression
# lambda function is a function that only needed/used in a short period of time
# it could be used as arguments in the higher order functions
# e.g. lmd = lambda x: x * 2

# map(function, sequence(list, tuple or strings))
# map function is used to apply a function to all the elements of a sequence
a = [1, 2, 3, 4]
b = [1, 1, 1, 1]


# map without lambda function
def sqr(x):
    return x ** 2


c = list(map(sqr, a))
print(c)


def list_add(x, y):
    return x + y


d = tuple(map(list_add, a, b))
print(d)

# map with lambda function
e = list(map(lambda x: x ** 2, a))
print(e)
f = tuple(map(lambda x, y: x + y, a, b))
print(f)
print()


# filter(function, sequence(list, tuple or strings))
# filter function is used to select elements from sequence using the provided function (which should return bool)


def test(x):
    return x % 2 == 0


g = list(filter(test, a))
print(g)

# filter with lambda function
h = list(filter(lambda x: x % 2 == 0, a))
print(h)
i = list(filter(lambda x: x ** 2 > 3, a))
print(i)
print()


# sorted(sequence(list, tuple or strings), key=function)
# sorted function sort the sequence using the result of the provided function
point2D = [(1, 5), (15, 1), (5, -1), (10, 4)]
point2D_sorted = sorted(point2D)  # sort by first value in tuple then the second value by default
print(point2D)
print(point2D_sorted)
point2D_sorted = sorted(point2D, key=lambda x: x[1])  # sort by the second value in tuple
print(point2D_sorted)
point2D_sorted = sorted(point2D, key=lambda x: x[0] + x[1])  # sort by the sum value in tuple
print(point2D_sorted)
print()


# reduce(function, sequence(list, tuple or string))
# reduce function apply the provided function (with two input) to the sequence and reduce it into one value
from functools import reduce
arr = [1, 2, 3, 4, 5, 6]
product_arr = reduce(lambda x, y: x * y, arr)
print(product_arr)
product_arr = reduce(lambda x, y: (y - x) ** 2, arr)
print(product_arr)
