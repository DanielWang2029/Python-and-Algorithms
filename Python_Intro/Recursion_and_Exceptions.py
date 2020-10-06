

# factorial
def factorial(n):
    try:  # try block will always be executed
        # assert statement, string to print if statement is False
        assert n >= 0, f'Input should not below 0. The value of input was {n}'
    except AssertionError as err:  # except block will be executed if type of error indicated has occur
        print(err)
    # could have several except clauses
    else:  # else block will be executed if type of error indicated has not occur
        if n == 1 or n == 0:
            return 1
        else:
            return factorial(n - 1) * n
    finally:  # finally block will always be executed even if type of error indicated has occur
        print('This will always be printed as it\'s in the \'finally\' block')


def factorial_2(n):
    if n < 0:
        # raise Exception(string to print)
        # this will end the execution and all the following code will not be executed
        raise Exception(f'Input should not below 0. The value of input was {n}')
    if n == 1 or n == 0:
        return 1
    else:
        return factorial_2(n - 1) * n


# could also raise self-define error:
class ValueTooHighError(Exception):
    def __init__(self, msg, value):
        self.msg = msg
        self.value = value

def test(x):
    if x > 10000:
        raise ValueTooHighError('Value is too high', x)

x = 12345

try:
    test(x)
except ValueTooHighError as err:
    print(err.msg, err.value)


x = factorial(5)
print(x)
y = factorial_2(5)
print(y)
p = factorial(-1)  # will not return since only code in except and finally block will be executed. Execution continues
print(p)  # due to factorial does not return, p is None
print('After p before q')  # this will be print as using try+except statement will not terminate the execution
# q = factorial_2(-1)  # an exception will be raised by raise Exception statement and execution ends immediately
# print(q)  # this code and below will not be executed due to the raise Exception statement in factorial_2
# print('After q')


# Fibonacci
def fib(n):
    try:
        assert n >= 1, f'Input should not below 1. The value of input was {n}'
    except AssertionError as err:
        print(err)
    else:
        if n == 1 or n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)


print(fib(-1))
print(fib(10))


# Fibonacci w/ dynamic programming
def fib_dynamic(n, memo):
    if len(memo) >= n:
        return memo[n - 1]
    elif n == 1 or n == 2:
        result = 1
    else:
        result = fib_dynamic(n - 1, memo) + fib_dynamic(n - 2, memo)
        memo.append(result)
    return result


import time
start_time = time.time()
print(fib_dynamic(35, [1, 1]))  # takes no time
print(time.time() - start_time)
start_time = time.time()
print(fib(35))  # takes about 5 seconds
print(time.time() - start_time)


def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [1, 1]
    for i in range(2, n):
        bottom_up.append(bottom_up[i - 1] + bottom_up[i - 2])
    return bottom_up[n - 1]


def fib_other_approach(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


# just amazing!
start_time = time.time()
print(fib_dynamic(500, [1, 1]))  # when n get larger, say 1000, python would raise a recursion error
print(time.time() - start_time)
start_time = time.time()
print(fib_bottom_up(500))  # no need to worry about the error here or below!
print(time.time() - start_time)
start_time = time.time()
print(fib_other_approach(500))
print(time.time() - start_time)
