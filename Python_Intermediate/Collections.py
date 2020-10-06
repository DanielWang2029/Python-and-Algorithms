

# collections: Counter, namedtuple, defaultdict, deque

from collections import Counter

x = 'aaaabbbccccc'
my_counter = Counter(x)
print(my_counter)  # a dict with different keys and their number of appearances, in decreasing order
print(my_counter.items())  # a list of keys and appearances in tuple
print(my_counter.keys())  # a list of keys
print(my_counter.values())  # a list of appearances
print(my_counter.most_common(2))  # a list of the first n most common keys and their appearances in tuple
print(list(my_counter.elements()))  # a list of elements
print()

from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)  # a Point with x = 1 and y = -4
print(pt)
print(pt.x, pt.y)  # value of x and y
print()

from collections import defaultdict

def_dict = defaultdict(float)  # input a type of the default dictionary
def_dict['a'] = 1
def_dict['b'] = 2
def_dict['c'] = 3
def_dict['d'] = 4
print(def_dict['e'])  # return the default value of the type instead of KeyError
print()

from collections import deque

deq = deque()
deq.append(1)
deq.append(2)
print(deq)
deq.appendleft(3)
print(deq)
deq.pop()
print(deq)
deq.popleft()
print(deq)
deq.clear()
print(deq)
deq.extend([4, 5, 6])  # 6 would be the right-most element
print(deq)
deq.extendleft([7, 8, 9])  # 9 would be the left-most element
print(deq)
deq.rotate(1)  # rotate the deque to the right by the input amount, minus number indicate rotate left
print(deq)
print()
