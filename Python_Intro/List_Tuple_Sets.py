

# List
courses = ['History', 'Math', 'Physics', 'CompSci']
print(len(courses))
print(courses)
print(courses[0])
print(courses[-1])
print(courses[-4])
print(courses[2:])

# insert
courses.append('Art')
print(courses)
courses.insert(0, 'Stat')
print(courses)
courses_another = ['Education', 'Communication']
courses_modify = courses.copy()
courses_modify.insert(0, courses_another)
print(courses_modify)
print(courses_modify[0])
courses.extend(courses_another)
print(courses)

# remove
courses.remove('Math')
print(courses)
removed = courses.pop()
print(courses)
print(removed)

# sort
courses.reverse()
print(courses)
nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
courses_sorted = sorted(courses)
print(courses_sorted)
print(courses)

# min max and sum
print(min(nums))
print(max(nums))
print(sum(nums))

# find
print(courses)
print(courses.index('CompSci'))
# print(courses.index('Math')) error
print('Art' in courses)
print('Math' in courses)

# loop
for course in courses:
    print(course)
for index, course in enumerate(courses):
    print(index, course)
for index, course in enumerate(courses, start=1):
    print(index, course)

# join and split
courses_str = ' - '.join(courses)
print(courses_str)
courses_new = courses_str.split(' - ')
print(courses_new)

# Tuple
# list is mutable (editable)
list_1 = [1, 2, 3, 4]
list_2 = list_1
print(list_1)
list_1[0] = 0
print(list_1)
print(list_2)

# tuple is immutable
tuple_1 = (1, 2, 3, 4, 5, 6)
tuple_2 = tuple_1
print(tuple_1)
# tuple_1[0] = 0 error

# Set
# only immutable object could be contained in a set
set_1 = {'Math', 'Stat', 'CompSci', 'Education'}
print(set_1)  # different result when execute multiple times
set_1 = {'Math', 'Stat', 'CompSci', 'Education', 'Math'}
print(set_1)
print('Math' in set_1)  # more optimal than list and tuple
set_2 = {'Math', 'Stat', 'Art', 'Design'}
print(set_2.intersection(set_1))
print(set_2.difference(set_1))
print(set_2.union(set_1))

# set is mutable
set_1.add('History')
set_1.remove('History')  # remove() works the same as discard() when the element to be deleted is in the set
set_1.discard('N/A')  # this works while set unchanged
# set_1.remove('N/A')  this fails and an KeyError will be raised


# create empty list tuple and sets
empty_list = []
empty_list_2 = list()
empty_tuple = ()
empty_tuple_2 = tuple()
empty_set = {}  # this is not correct, it's a dictionary
empty_set_2 = set()  # this is correct
empty_set_3 = set('Hello')  # this is also correct, but returns a set w/ 'H' 'e' 'l' 'o' as its elements
# empty_set_4 = set('Hello', 'Hi')  this is incorrect as creating a set using set() could only have one input

# additional info from another video
list1 = [1, 2, 3, 4, 5, 6, 7]
list1.pop()
print(list1)
list1.pop(2)
print(list1)
list1[0], list1[1] = list1[1], list1[0]  # a new way to swap
print(list1)

# a new way to initialize a list
a = list(range(1, 5))  # range(a, b) include a but does not include b
print(a)

# list comprehensions
# [expression for item in iterable]
a = [1, 3, 5, 7, 9]  # want b = [2, 6, 10, 14, 18]
print(a)
b = 2 * a  # list consist two list a
print(b)
b = [x * 2 for x in a]
print(b)
c = [x ** 2 for x in range(7)]
print(c)
d = [x ** 2 for x in reversed(range(7))]
print(d)
e = [x + y for x in a for y in b]
print(e)
f = [a[i] + b[i] for i in range(len(a))]
print(f)

# [expression for item in iterable if conditional]
# [expression if conditional else statement for item in iterable]
g = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(g)
h = [x ** 2 if x > 4 else x ** 3 for x in range(1, 11)]
print(h)

# double for loop list comprehensions
# [expression for y in x for z in y] === for y in x: for z in y: expression
# Rule of thumb: the order of fors in the comprehension is the same as the order of the nested loops
i = [(x, y) for x in [1, 2] for y in [3, 4]]
print(i)  # print [(1, 3), (1, 4), (2, 3), (2, 4)]
