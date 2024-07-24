

# Dictionary
# only immutable object could be the key but the value could be mutable
student = {'name': 'John', 'age': 25, 'course': ['Math', 'Stat'], 1: 111}

# Retrieve
print(student['name'])
print(student['course'])
print(student[1])
# print(student[2]) KeyError
print(student.get(1))
print(student.get(2))
print(student.get(2, 'Not Found'))

# Add
student['phone'] = '(555)555-5555'  # add
print(student.get('phone'))
student['age'] = 30  # update
print(student.get('age'))
student.update({'name': 'Jane', 1: 222, 'hobby': 'skiing'})  # add and update
print(student)

# Delete
del student['age']
print(student)
name = student.pop('name')
print(student)
print(name)

# Loop
print(len(student))  # length of keys
print(student.keys())
print(student.values())
print(student.items())
for key, value in student.items():
    print(key, value)
for item in student.items():
    print(item)
    print(type(item))


# Dictionary comprehension
d = {k:v for k, v in enumerate([1, 3, 5, 7, 9])}
print(d)  # prints {0:1, 1:3, 2:5, 3:7, 4:9}

# can also initialize using dict() with a iterables of iterables where each element has size of 2
d = dict(((1, 2), (3, 4), (5, 6)))
print(d)  # prints {1:2, 3:4, 5:6}

# initialize using dict() and zip() with a key list and a value list
d = dict(zip([0, 1, 2], [3, 4, 5]))
print(d)  # prints {0:3, 1:4, 2:5}
