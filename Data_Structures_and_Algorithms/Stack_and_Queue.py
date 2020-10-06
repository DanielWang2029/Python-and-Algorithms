

import copy


# Stack
class Stack:
    def __init__(self, *args):
        self.arr = list()
        for elm in args:
            self.arr.append(elm)

    # [bottom, ... , top] <-> push and pop
    def push(self, elm):
        self.arr.append(elm)

    def pop(self):
        try:
            assert not self.isEmpty(), 'The stack is empty. Could not pop any element. Returning None'
        except AssertionError as err:
            print(err)
            return None
        else:
            return self.arr.pop()

    def top(self):
        try:
            assert not self.isEmpty(), 'The stack is empty and no top element exist. Returning None'
        except AssertionError as err:
            print(err)
            return None
        else:
            return self.arr[-1]

    def bottom(self):
        try:
            assert not self.isEmpty(), 'The stack is empty and no bottom element exist. Returning None'
        except AssertionError as err:
            print(err)
            return None
        else:
            return self.arr[0]

    def isEmpty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)

    def getList(self):
        return self.arr

    def copy(self):
        return Stack(*self.arr)

    def __str__(self):
        return str(self.arr)

    def __len__(self):
        return len(self.arr)

    # other could be Stack or list
    def __eq__(self, other):
        if type(other) == list and self.size() == len(other):
            for index, value in enumerate(self.arr):
                if value != other[index]:
                    return False
        elif type(other) == Stack and self.size() == other.size():
            for index, value in enumerate(self.arr):
                if value != other.getList()[index]:
                    return False
        else:
            return False
        return True

    def __iadd__(self, other):
        if type(other) == Stack:
            self.arr.extend(other.getList())
        else:
            self.push(other)
        return self

    # default self will be 'under' other
    def __add__(self, other):
        temp_arr = self.arr.copy()
        if type(other) == Stack:
            temp_arr.extend(other.getList())
        else:
            temp_arr.append(other)
        return Stack(*temp_arr)

    def __radd__(self, other):
        return Stack.__add__(self, other)

    # link for shallow copy and deep copy: https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/copy/index.html
    def __copy__(self):
        return Stack(*self.arr)


# test cases
# s1 = Stack(1, 2, 3)
# s2 = copy.copy(s1)
# s1 += 10
# s1 = s1 + 4
# s1 = 5 + s1
# s3 = s1 + s2
# s1.push(s3.pop())
# print(s1, s2, s3)
# s1.pop()
# s3.pop()
# print([1, 2, 3, 10, 4, 5] == s1, s3 == s1)
# s3.pop()
# print(s3 == s1)

# Queue
class Queue:
    def __init__(self, *args):
        self.arr = list()
        for elm in args:
            self.arr.append(elm)

    # dequeue or pop <- [top, ... , bottom] <- enqueue or push
    def push(self, elm):
        self.arr.append(elm)

    def enqueue(self, elm):
        self.push(elm)

    def pop(self):
        try:
            assert not self.isEmpty(), 'The queue is empty. Could not pop any element. Returning None'
        except AssertionError as err:
            print(err)
            return None
        else:
            return self.arr.pop(0)

    def dequeue(self):
        return self.pop()

    def top(self):
        try:
            assert not self.isEmpty(), 'The queue is empty and no top element exist. Returning None'
        except AssertionError as err:
            print(err)
            return None
        else:
            return self.arr[0]

    def bottom(self):
        try:
            assert not self.isEmpty(), 'The queue is empty and no bottom element exist. Returning None'
        except AssertionError as err:
            print(err)
            return None
        else:
            return self.arr[-1]

    def isEmpty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)

    def getList(self):
        return self.arr

    def copy(self):
        return Queue(*self.arr)

    def __str__(self):
        return str(self.arr)

    def __len__(self):
        return len(self.arr)

    # other could be Queue or list
    def __eq__(self, other):
        if type(other) == list and self.size() == len(other):
            for index, value in enumerate(self.arr):
                if value != other[index]:
                    return False
        elif type(other) == Queue and self.size() == other.size():
            for index, value in enumerate(self.arr):
                if value != other.getList()[index]:
                    return False
        else:
            return False
        return True

    def __iadd__(self, other):
        if type(other) == Queue:
            self.arr.extend(other.getList())
        else:
            self.push(other)
        return self

    # default self will be 'left to' other
    def __add__(self, other):
        temp_arr = self.arr.copy()
        if type(other) == Queue:
            temp_arr.extend(other.getList())
        else:
            temp_arr.append(other)
        return Queue(*temp_arr)

    def __radd__(self, other):
        return Queue.__add__(self, other)

    def __copy__(self):
        return Queue(*self.arr)


# test cases
# s1 = Queue(1, 2, 3)
# s2 = copy.copy(s1)
# s1 += 10
# s1 = s1 + 4
# s1 = 5 + s1
# s3 = s1 + s2
# s1.push(s3.pop())
# print(s1, s2, s3)
# s1.pop()
# print([2, 3, 10, 4, 5, 1] == s1, s3 == s1)
# s3 = s1.copy()
# print(s1 == s3)
