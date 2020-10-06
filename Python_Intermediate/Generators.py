

def my_generator():
    print("been here 1")
    yield 1  # a stop point for next(), return 1 and pause
    print("been here 2")
    yield 2
    print("been here 3")
    yield 3
    print("been here 4")  # don't do this because this could not be reached using next() (treat yield as return)


g = my_generator()  # this line does not execute the my_generator function

print("begin next")
print()

value = next(g)  # execute to the next (in this case first) yield statement, return yield value and pause
print(value)  # print 1

value = next(g)
print(value)  # print 2

value = next(g)
print(value)  # print 3

# value = next(g)  # raise a StopIteration error as no further yield statement
# print(value)

print()


# another way to go through my_generator
# note that this execute the code after the last yield statement
h = my_generator()

for i in h:
    print(i)
print()


# generator is an iterable so many function could be implement on it
p = my_generator()
print(sum(p))

q = my_generator()
print(sorted(q, reverse=True))
print()


# another example
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)  # again this does not execute countdown

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
# print(next(cd))  # raise a StopIteration error
print()


# example on space/memory complexity
import sys


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums  # memory complexity O(n)


print(sum(firstn(10)))


def firstn_generator(n):
    num = 0
    while num < n:
        yield num  # memory complexity O(1)
        num += 1


print(sum(firstn_generator(10)))

print(sys.getsizeof(firstn(100000)))  # the size grows larger with increasing n
print(sys.getsizeof(firstn_generator(100000)))  # the size is the same
print()


# generator comprehension
generator = (i for i in range(10) if i % 2 == 0)  # use () instead of [] for list comprehension
for i in generator:
    print(i)
print()


# another example on memory complexity compared to list
n = 100000
generator = (i for i in range(n) if i % 2 == 0)
mylist = [i for i in range(n) if i % 2 == 0]

print(sys.getsizeof(mylist))  # again this grows larger with increasing n
print(sys.getsizeof(generator))  # this is constant
