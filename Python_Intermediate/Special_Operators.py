
# := is an assignment expression, similar to =
# This is only valid for python >= 3.8
y = (x := 9)  # this is equivalent to y = x = 9
print(x, y)  # prints 9, 9

# suppose we have three functions and we need to calculate k(f/g(x)) if f/g(x) is not None else k(x)
def f(x):
  # some complicated computation here

def g(x):
  # some complicated computation here

def k(x):
  # some complicated computation here

# without :=
fx = f(x)
if fx:
  result = k(fx)
else:
  gx = g(x)
  if gx:
    result = k(gx)
  else:
    result = k(x)

# with :=
if (fx := f(x)):
  result = k(fx)
elif (gx := g(x)):
  result = k(gx)
else:
  result = k(x)

# we can also use := when the value is expensive to compute
arr = [z := f(g(k(z))), z**2, z**3]

# note that the scope for := is the currently scope (honors nonlocal/global declarations)
# except in comprehensions where it actually binds the target with the outer scope
# this means that variables defined in list comprehension exist outside the comprehension
print(z)  # prints f(g(k(x))), not raising an exception

# another example for the exception
total = 0
left_sum = [total := total + v for v in range(10)]
print(total)  # prints 45

# an example for for/while loops
k = 0
while (n := k) in range(m := 9):
    k += 1
    continue
print(n, m)  # prints 9, 9

# an example for nonlocal declarations
f = lambda n : [(x := y) for y in range(n)]
g = f(10)
print(x)  # raises NameError exception, because y is a nonlocal variable inside a lambda function

# other invalid cases (all raises SyntaxError）
y := f(x)  # unparenthesized assignment expressions are prohibited at the top level of an expression statement
[i := 0 for i, j in range(10)]  # cannot assign a value to nonlocal variables
[i for i in (j := range(10)]  # named expressions are disallowed entirely as part of comprehension iterable expressions
