
# What is a namespace in python
# According to python docs: "A namespace is a mapping from names to objects"
# The object here could be variables, functions, classes etc.
# Most namespaces are currently implemented as Python dictionaries

# For example:
x, y, z = 0, [1, 2], {3, 4, 5}
# the namespace for current scope (excluding default keywords and variables like None, class, list etc.) is
namespace = {'x': 0, 'y': [1, 2], 'z': {3, 4, 5}}


# What is a scope in python
# According to python docs: "A scope is a textual region of a Python program where a namespace is directly accessible."
# Basically a scope is a region within some code chunks where access to namespaces are the same

# Here's a typical structure of the scopes:
# the innermost scope, which is searched first, contains the local names (assignments to names always go into the innermost scope)
# the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
# the next-to-last scope contains the current module’s global names (this is the global scope, but not the outermost)
# the outermost scope (searched last) is the namespace containing built-in names (this namespace usually don't change)

# For example:
x = 0
# global scope
# here the scope corresponding to the namespace {'x': 0}
for i in [1]:
    # non-local, non-global scope
    # here the scope corresponding to the namespace {'x': 0, 'i': 1}
    def f():
        y = True
        return y
        # innermost scope
        # here the scope corresponding to the namespace {'x': 0, 'i': 1, 'y': True}
    pass


# In general, all variables found outside of the innermost scope are read-only
# i.e. an attempt to write to such a variable will simply create a new local variable in the innermost scope,
# leaving the identically named outer variable unchanged:
x = 0
def f():
    x = 1  # this creates a local variable x that points to 1, does not change the value of global x
f()
print(x)  # prints 0


# How does keyword global work
# global keyword allows the binding of variable between local and global scope:
x = 0
def f():
    global x  # this binds local x with global x
    x = 1  # this changes the local x as well as global x
f()
print(x)  # prints 1


# global cannot be used on previously defined local variable:
x = 0
def f():
    x = 1
    global x  # raise SyntaxError: name 'x' is assigned to before global declaration


# global could be used on variables that are not defined in global scope:
def f():
    global g  # this binds local g with global g
    g = 1  # this changes the local g as well as global g
f()
print(g)  # prints 1, although there's never been a definition of g in global scope


# only the global scope will be bind with local scope:
x = 0
def outer():
    x = 1
    def inner():
        global x  # only binds x between inner with global, leaving outer unchanged
        x = 2  # change x in inner and global scope
        print("inner:", x)  # prints inner: 2
    inner()
    print("outer:", x)  # prints outer: 1
outer()
print("global:", x)  # prints global: 2


# How does keyword nonlocal work
# nonlocal keyword allows the binding of variable between local and the outer (but non-global) scope:
x = 0
def outer():
    x = 1
    def middle():
        x = 2
        def inner():
            nonlocal x  # binds x between inner and middle
            x = 3  # change x in inner and middle scope
            print("inner:", x)  # prints inner: 3
        inner()
        print("middle:", x)  # prints middle: 3
    middle()
    print("outer:", x)  # prints outer: 1, outer is two level out of inner therefore it does not get bind with inner
outer()
print("global:", x)  # prints global: 0


# nonlocal will search for outer (non-global) scope until one of them contains the variable:
x = 0
def outer():
    x = 1  # outer scope is the first outer scope that contains x
    def middle():
        y = 2  # middle scope does not have a declaration of x
        def inner():
            nonlocal x  # binds x between inner and outer
            x = 3  # change x in inner and outer scope
            print("inner:", x)  # prints inner: 3
        inner()
    middle()
    print("outer:", x)  # prints outer: 3
outer()
print("global:", x)  # prints global: 0


# multiple nonlocal can work together:
x = 0
def outer():
    x = 1
    def middle():
        nonlocal x  # binds middle x with outer x
        x = 2
        def inner():
            nonlocal x  # binds x between inner and middle
            x = 3  # change x in inner and middle scope
            print("inner:", x)  # prints inner: 3
        inner()
        print("middle:", x)  # prints middle: 3
    middle()
    print("outer:", x)  # prints outer: 3
outer()
print("global:", x)  # prints global: 0


# nonlocal cannot bind local with global:
x = 0
def f():
    nonlocal x  # raise SyntaxError: no binding for nonlocal 'x' found

x = 0
def f():
    def g():
        nonlocal x  # raise SyntaxError: no binding for nonlocal 'x' found


# nonlocal cannot be used on previously defined local variable:
def outer():
    x = 1
    def inner():
        x = 2
        nonlocal x  # raise SyntaxError: name 'x' is assigned to before nonlocal declaration


# A side note: del delete variable in local as well as in its binding scope:
def f():
    x = 1
    def g():
        nonlocal x
        del x
    print(x)  # raise UnboundLocalError: local variable 'x' referenced before assignment

x = 0
def f():
    global x
    del x
f()
print(x)  # raise NameError: name 'x' is not defined
