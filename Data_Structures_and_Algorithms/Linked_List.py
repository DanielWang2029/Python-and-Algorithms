

from typing import List
from Data_Structures_and_Algorithms.Stack_and_Queue import Stack


# linked list only have next, double linked list have next and prev
class Node:
    def __init__(self, data=-1, following=None):
        self._data = data
        self._next = following

    def setNext(self, following=None):
        try:
            assert type(following) == Node or following is None, 'Could not set next to type other than Node and None'
        except AssertionError as err:
            print(err)
        else:
            self._next = following

    def setData(self, data):
        self._data = data

    def getData(self):
        return self._data

    def getNext(self):
        return self._next

    def __add__(self, other: int):
        try:
            assert type(other) == int, 'Could not implement __add__ on type other than int. Returning None'
        except AssertionError as err:
            print(err)
            return None
        currentNode = self
        for _ in range(other):
            try:
                assert currentNode is not None, 'Invalid Input. Run out of Nodes. Returning None'
            except AssertionError as err:
                print(err)
                return None
            currentNode = currentNode.getNext()
        return currentNode

    def __iadd__(self, other: int):
        return self.__add__(other)

    def __radd__(self, other: int):
        return self.__add__(other)


first = Node(6)
second = Node(3)
third = Node(4)
fourth = Node(2)
fifth = Node(1)
first.setNext(second)
second.setNext(third)
third.setNext(fourth)
fourth.setNext(fifth)
# print(first.next.next.next.next.data)
# print(first.next.next.next.data)
# print(first.next.next.data)
# print(first.next.data)
# print(first.data)
current = 3 + first
print(current.getData())
current += 1
print(current.getData())
current = current + 1
print(current)
print()


class LinkedList:
    def __init__(self, *args):
        self.head = None
        previous_node = None
        for index, value in enumerate(args):
            current_node = Node(value)
            if index == 0:
                self.head = current_node
            else:
                previous_node.setNext(current_node)
            previous_node = current_node

    def getNode(self, index: int) -> Node:
        try:
            assert self.length() > index, "Invalid index. Input is larger or equal to the length of the linked list"
            assert index >= 0, "Invalid index. Input is less than zero"
        except AssertionError as err:
            print(err)
        else:
            return self.head + index

    def length(self) -> int:
        currentNode = self.head
        x = 0
        while currentNode is not None:
            x += 1
            currentNode = currentNode.getNext()
        return x

    def printList(self):
        currentNode = self.head
        result = []
        while currentNode is not None:
            result.append(currentNode.getData())
            currentNode = currentNode.getNext()
        print(result)

    def getNodeList(self) -> List[Node]:
        currentNode = self.head
        result = []
        while currentNode is not None:
            result.append(currentNode)
            currentNode = currentNode.getNext()
        return result

    def insert_front(self, thing):
        self.insert_multiple(0, thing)

    def insert_end(self, thing):
        self.insert_multiple(self.length(), thing)

    def insert(self, index: int, thing):
        self.insert_multiple(index, thing)

    def insert_multiple(self, index: int, *args):
        try:
            assert self.length() >= index, "Invalid index. Input is larger than the length of the linked list"
            assert index >= 0, "Invalid index. Input is less than zero"
        except AssertionError as err:
            print(err)
            return
        currentNode = self.head
        # dealing with LinkedList that is initially empty or insertion at the front
        if currentNode is None or index == 0:
            nextNode = currentNode if currentNode is not None else None
            for ind, value in enumerate(args):
                if ind == 0:
                    currentNode = Node(value)
                    self.head = currentNode
                else:
                    currentNode.setNext(Node(value))
                    currentNode += 1
            if nextNode is not None:
                currentNode.setNext(nextNode)
            return
        currentNode += index - 1
        nextNode = currentNode.getNext()
        for value in args:
            currentNode.setNext(Node(value))
            currentNode += 1
        currentNode.setNext(nextNode)

    def delete_front(self) -> Node:
        return self.delete_multiple(0, 1)[0]

    def delete_end(self) -> Node:
        return self.delete_multiple(self.length() - 1, 1)[0]

    def delete(self, index: int) -> Node:
        return self.delete_multiple(index, 1)[0]

    def delete_multiple(self, index: int, number: int) -> List[Node]:
        try:
            assert index < self.length(), "Invalid index. Input is larger or equal to the length of the linked list"
            assert index >= 0, "Invalid index. Input is less than zero"
        except AssertionError as err:
            print(err)
            return []
        try:
            assert index + number <= self.length(), "Input number exceed the maximum that could be deleted. " \
                                                   "Deleting all following Nodes from input index"
        except AssertionError as err:
            print(err)
            number = self.length() - index
        currentNode = self.head
        # dealing with front deletion
        if index == 0:
            result = []
            for _ in range(number):
                result.append(currentNode)
                # tempNode = currentNode
                currentNode += 1
                # del tempNode
            self.head = currentNode
            return result
        currentNode += index - 1
        nextNode = currentNode.getNext()
        result = []
        for _ in range(number):
            result.append(nextNode)
            # tempNode = nextNode
            nextNode += 1
            # del tempNode
        currentNode.setNext(nextNode)
        return result

    def reverse(self):
        prevNode = None
        currentNode = self.head
        while currentNode is not None:
            tempNode = currentNode.getNext()
            currentNode.setNext(prevNode)
            prevNode = currentNode
            currentNode = tempNode
        self.head = prevNode

    def reverse_recursion(self):
        if self.head is not None:
            self.head = self._reverse_recursion_helper(self.head)

    @ staticmethod
    def _reverse_recursion_helper(currentNode: Node) -> Node:
        if currentNode.getNext() is None:
            return currentNode
        result = LinkedList._reverse_recursion_helper(currentNode.getNext())
        currentNode.getNext().setNext(currentNode)
        currentNode.setNext(None)
        return result

    def reverse_stack(self):
        stk = Stack(*self.getNodeList())
        if stk.isEmpty():
            self.head = None
            return
        self.head = stk.top()
        while not stk.isEmpty():
            currentNode = stk.pop()
            currentNode.setNext(stk.top())
        del stk

    def __len__(self):
        return self.length()


newLinkedList = LinkedList()
newLinkedList.insert_multiple(0, *[0, 3, 6, 9])  # remember to add the * in front of the list representing args
newLinkedList.printList()
newLinkedList.insert(2, 4)
newLinkedList.printList()
newLinkedList.insert(3, 5)
newLinkedList.printList()
newLinkedList.insert_multiple(5, *[7, 8])
newLinkedList.printList()
newLinkedList.insert_front(-3)
newLinkedList.printList()
newLinkedList.insert_end(12)
newLinkedList.printList()
newLinkedList.insert_multiple(10, *[15, 18])
newLinkedList.printList()
newLinkedList.insert_multiple(0, *[-9, -6])
newLinkedList.printList()
print(newLinkedList.length())
print()

print(newLinkedList.delete_end().getData())
newLinkedList.printList()
print(newLinkedList.delete_front().getData())
newLinkedList.printList()
print(newLinkedList.delete(1).getData())
newLinkedList.printList()
print(newLinkedList.delete_multiple(3, 5)[0].getData())
newLinkedList.printList()
print(newLinkedList.delete_multiple(2, 100)[0].getData())
newLinkedList.printList()
print(newLinkedList.delete_multiple(0, 2)[0].getData())
newLinkedList.printList()
newLinkedList.insert(0, 66)
print(newLinkedList.delete_front().getData())
newLinkedList.printList()
newLinkedList.insert(0, 99)
print(newLinkedList.delete_end().getData())
newLinkedList.printList()
print()

newLinkedList.insert_multiple(0, *[1, 2, 3, 4, 5, 6, 7])
newLinkedList.reverse()
newLinkedList.printList()
newLinkedList.reverse_recursion()
newLinkedList.printList()
newLinkedList.reverse_stack()
newLinkedList.printList()
