

# Conditionals
language = 'Python'
language_another = language
language_third = ''
language_third += 'Python'
if language == 'Python':
    print('1st condition is true')
elif language == 'Java':
    print('Java!')
else:
    print('1st condition is not true')
if language is language_another:
    print('2nd condition is true')
if language is language_third:
    print('3rd condition is true')

print(id(language))
print(id(language_another))
print(id(language_third))

user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log in')
elif user == 'Admin':
    print('Welcome')

condition = None  # 0, '', [], {}, () also evaluated to False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 'Python_Fundamentals'  # all the stuff not listed above is evaluated to True
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# an example of the content above
for i in range(1, 10):
    if i % 3:
        print(i)


x = 5
# positive value if expression else negative value
print(1 if x > 10 else 2)
print()

# or in python

# or statement uses short-circuit evaluation, meaning once a True is find, the rest will not be evaluated

# when x and y are objects, x or y returns x if it evaluates to true, otherwise returns y
# when multiple objects are involved, or statement returns the first true operand it finds, or the last one
#     note that an object is considered true unless its class defines
#     1. a __bool__() that returns False or
#     2. a __len__() that returns zero

print(1 == 1 or [] or 'P')  # print True
print('x' or [] or 'P')  # print 'x' as it evaluates to true
print(1 == 2 or [1] or 'P')  # print [1]
print(1 == 2 or [] or 'P')  # print 'P'
print(1 == 2 or [] or '' or None)  # print None, even if None evaluates to false
print()

# if x is an expression and y is an object, the return value follows the rule above:
#  Exp   Object  Result      e.g.
#  True   True    True            2 < 4 or 2 returns True
#  True   False   True            2 < 4 or [] returns True
#  False  False  Object           2 > 4 or [] returns []
#  False  True   Object           2 > 4 or 4 returns 4

# application of this quality: var or default for function input
arr = list()
# max(arr)  ValueError: max() arg is an empty sequence
print(max(arr or [-1]))  # this works fine
