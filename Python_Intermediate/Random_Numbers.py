

import random

a = random.random()  # float from 0 to 1
print(a)
b = random.uniform(1, 10)  # float from 1 to 10
print(b)
c = random.randint(1, 10)  # upper bound included
print(c)
d = random.randrange(1, 10)  # upper bound not included
print(d)
e = random.normalvariate(0, 1)  # random normal with provided mean and variance
print(e)
print()

my_list = list("ABCDEFG")
f = random.choice(my_list)
print(f)
g = random.sample(my_list, 3)  # unique sample (without replacement)
print(g)
h = random.choices(my_list, k=5)  # non-unique sample (with replacement)
print(h)
random.shuffle(my_list)
print(my_list)
print()

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())  # same as seed 1
print(random.randint(1, 10))
random.seed(2)
print(random.random())  # same as seed 2
print(random.randint(1, 10))
print()

import secrets  # used for security purposes, takes longer time
x = secrets.randbelow(10)  # random int from 0 to 9, upper bound not included
print(x)
y = secrets.randbits(5)  # return a binary representation of an int with given number of bits
# e.g. 10001, which is 17
print(y)
my_list = list("ABCDEFG")
z = secrets.choice(my_list)
print(z)
print()

import numpy as np
p = np.random.rand(3)  # a np array of length n with random float from 0 to 1
print(p)
p = np.random.rand(3, 3)  # a np array of provided args shape with random float from 0 to 1
print(p)
q = np.random.randint(0, 10, 3)  # a np array of length n with random int from 0 to 10, upper bound not included
print(q)
q = np.random.randint(0, 10, (4, 5))  # a np array of provided tuple shape
print(q)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
np.random.shuffle(arr)  # shuffle in the first x axis
print(arr)
print()

np.random.seed(1)  # use np.random.seed() instead of random.seed()
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))  # same as seed 1
