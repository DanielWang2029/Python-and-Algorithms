

message = "Daniel's World"
message_another = 'Daniel\'s World'
message_other = """Daniel's World was a good
cartoon in the 1990s"""
print(message)
print(message_another)
print(message_other)

print(len(message))
print(message[0])
print(message[0:6])
print(message[9:])

print(message.lower())
print(message.upper())

print(message.count('l'))
print(message.find('World'))
print(message.find('world'))

message_new = message.replace('World', 'Universe')
print(message_new)

greeting = 'Hello'
name = 'Daniel'

message_pretty_new = greeting + ', ' + name + ". Welcome!"
message_so_new = '{}, {}. Welcome!'.format(greeting, name)
print(message_pretty_new)
print(message_so_new)

message_f = f'{greeting}, {name}. Welcome!'
print(message_f)

print(help(str.lower))

# Advanced f String
import random

class FuzzyTriangleArea:

    def __init__(self, p=0.8, v=0.1):
        self.p, self.v = p, v

    def __call__(self, a, b, c):
        p = (a + b + c) / 2
        result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        if random.random() <= self.p:
            return result
        else:
            return random.uniform(result - self.v,
                                  result + self.v)


area1 = FuzzyTriangleArea()
area2 = FuzzyTriangleArea(0.5, 0.2)
for i in range(12):
    print(f"{area1(3, 4, 5):4.3f}, {area2(3, 4, 5):4.2f}")
# In the above line, ':4' means the length of the output is at least 4
# ':.3f' means keep 3 decimal places for the floating point number
# together it's ':4.3f'
# other special notations like ':e' represent scientific could be found at 'http://zetcode.com/python/fstring/'
