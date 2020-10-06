

from Data_Structures_and_Algorithms.Stack_and_Queue import Stack
from typing import List


# Infix (w/ binary operator, i.e. two operand)
# <operand> <operator> <operand>
# e.g. 2 + 3, A - B, (2 + 3) * (p + q)

# Order of operation
# 1. Parentheses
# 2. Exponents
# 3. Multiplication and Division
# 4. Addition and Subtraction

# Prefix
# <operator> <operand> <operand>
# e.g. + 2 3, - A B, * + 2 3 + p q

# Postfix
# <operand> <operand> <operator>
# e.g. 2 3 +, A B -, 2 3 + p q + *

def evaluate_postfix(*args):
    stk = Stack()
    for value in args:
        if type(value) == str:
            x = stk.pop()
            y = stk.pop()
            if x is None or y is None:
                assert False, f'Invalid Input. Wrong input sequence detected for operator "{value}"'
            if value == '+':
                stk.push(y + x)
            elif value == '-':
                stk.push(y - x)
            elif value == '*':
                stk.push(y * x)
            elif value == '/':
                stk.push(y / x)
            elif value == '**' or value == '^':
                stk.push(y ** x)
            else:
                assert False, 'Invalid Input. No such operator found'
        else:
            stk.push(value)
    assert len(stk) == 1, 'Error'
    result = stk.pop()
    del stk
    return result


def evaluate_prefix(*args):
    stk = Stack()
    arr = list(args)
    arr.reverse()
    for value in arr:
        if type(value) == str:
            x = stk.pop()
            y = stk.pop()
            if x is None or y is None:
                assert False, f'Invalid Input. Wrong input sequence detected for operator "{value}"'
            if value == '+':
                stk.push(x + y)
            elif value == '-':
                stk.push(x - y)
            elif value == '*':
                stk.push(x * y)
            elif value == '/':
                stk.push(x / y)
            elif value == '**' or value == '^':
                stk.push(y ** x)
            else:
                assert False, 'Invalid Input. Input operator not found'
        else:
            stk.push(value)
    assert len(stk) == 1, 'Error'
    result = stk.pop()
    del stk
    return result


def infix_to_postfix(*args) -> List:
    stk = Stack()
    result = []
    for value in args:
        if type(value) == str:
            if value != '(' and value != ')':
                # note that is_equal is not included because for +- and */ left to right or right to left do not matter
                # however for ** and ^, the default sequence is right to left
                # this means 1 ** 2 ** 3 = 1 ** (2 ** 3) = 1 ** 8 = 1, not 8
                while (not stk.isEmpty()) \
                        and is_higher(value, stk.top()) \
                        and stk.top() != '(':
                    result.append(stk.pop())
                stk.push(value)
            elif value == ')':
                while stk.top() != '(':
                    result.append(stk.pop())
                stk.pop()
            else:
                stk.push(value)
        else:
            result.append(value)
    while not stk.isEmpty():
        result.append(stk.pop())
    return result


def is_higher(x: str, y: str) -> bool:
    if x == '+' or x == '-':
        return y == '*' or y == '/' or y == '**' or y == '^'
    elif x == '*' or x == '/':
        return y == '**' or y == '^'
    elif x == '**' or x == '^':
        return False
    else:
        assert False, 'Invalid Input. Input operator not found'


def is_equal(x: str, y: str) -> bool:
    if x == '+' or x == '-':
        return y == '+' or y == '-'
    elif x == '*' or x == '/':
        return y == '*' or y == '/'
    elif x == '**' or x == '^':
        return y == '**' or y == '^'
    else:
        assert False, 'Invalid Input. Input operator not found'


print(evaluate_postfix(*[3, 1, 1, '+', '^', 2, '**', 80, '-']))
print(evaluate_prefix(*['^', '-', '+', '*', 2, 3, '+', 5, 4, 9, 2]))
print(infix_to_postfix(*[2, '+', 3, '*', 4, '^', 5, '^', 6, '/', 7, '-', 8]))
print(infix_to_postfix(*['(', 2, '+', 3, ')', '*', 4, '^', 5, '^', '(', 6, '/', 7, ')', '-', 8]))
arr = infix_to_postfix(*['(', 2, '+', 3, ')', '*', 2, '^', 2, '^', '(', 6, '/', '(', 8, '-', 6, ')', ')', '+', 9])
print(infix_to_postfix(*arr))
print(evaluate_postfix(*infix_to_postfix(*arr)))
print((2 + 3) * 1 ** 2 ** (2 / (7 - 6)) + 9)  # note that ** by default goes from right to left
