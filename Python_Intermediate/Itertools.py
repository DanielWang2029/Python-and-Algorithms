

# itertools: product, permutations, combinations, accumulate, groupby and infinite iterators

from itertools import product

a = [1, 2]
b = [3]
prod = product(a, b)  # a list of elements in the Cartesian product of a and b (A x B in math)
print(list(prod))
prod = product(a, b, repeat=2)
print(list(prod))
print()

from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)  # a list of tuple of different permutations of a
print(list(perm))
print()

from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]
comb = combinations(a, 2)  # a list of tuple of different combinations (without replacement) of a
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)  # a list of tuple of different combinations (with replacement) of a
print(list(comb_wr))
print()

from itertools import accumulate
import operator

a = [1, 2, 3, 4, 3, 2, 1]
acc = accumulate(a)  # a list of accumulated sums by default
print(a)
print(list(acc))
acc_mul = accumulate(a, func=operator.mul)  # a list of accumulated products
print(list(acc_mul))
acc_max = accumulate(a, func=max)  # a list of accumulated max
print(list(acc_max))
print()

from itertools import groupby

a = [1, 1, 2, 2, 3, 3, 4, 4]
gb = groupby(a, key=lambda x: x)  # group by boolean
for key, value in gb:
    print(key, list(value), end=" ")
print()
gb = groupby(a, key=lambda x: x < 3)  # group by value
for key, value in gb:
    print(key, list(value), end=" ")
print()
print()

from itertools import count, cycle, repeat

for i in count(10):  # infinite loop that start at 10
    print(i, end=" ")
    if i == 15:
        print()
        break

a = [1, 2, 3]
counter = 0
for i in cycle(a):  # infinite cycle of elements in a
    print(i, end=" ")
    counter += 1
    if counter > 10:
        print()
        break

for i in repeat(1, 15):  # repeat elements by the given number of times
    print(i, end=" ")
print()
