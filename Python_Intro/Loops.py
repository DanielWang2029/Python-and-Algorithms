

# Loops
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 2:
        continue
    print(num)
    if num == 4:
        print('Found')
        break

for i in range(10):
    print(i)

x = 0
while x < 10:
    print(x)
    x += 1

# From list
courses = ['Math', 'Stat', 'Com_Sci', 'Econ']
for course in courses:
    print(course)
for index, course in enumerate(courses):
    print(index, course)
for index, course in enumerate(courses, start=1):
    print(index, course)
