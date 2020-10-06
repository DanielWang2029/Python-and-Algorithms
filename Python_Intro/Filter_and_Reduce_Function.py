

# filter(function, iterables)
# filter function return (as filter object) the elements from the iterables for which the input function become true
a = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(a)

# reduce(function, iterables)
# reduce function reduce a iterable to a single element using some function
import functools

num = [1, 2, 3, 4]
print(functools.reduce(lambda x, y: x + y, num))
