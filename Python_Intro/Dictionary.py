

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

# from another video
d = {1: 100, 2: 200}
# del d[3]  KeyError
print(d)