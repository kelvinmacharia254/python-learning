'''
Python function are also objects stored in memory

Function can be passed around a program.
They can called indirectly.

They support attributes and annotations.

'''

print("1. Function are just like any other object in Python")
def print_name(name):
    print(f"Hello, I am {name}.")

func = print_name # Assign function to a variable just like any other object

func("Goodluck") # Call the function using the variable

print("2. Function attributes")
print("2(a) Simple argument attributes")
def print_age(age):
    print(f"I am {age} years old")

def indirect(func, arg): # pass function as argument
    func(arg)
    
indirect(print_age, 25) # Call the function indirectly

print("2(b) Function attributes in data structure")

lst = [(print_name, "Goodluck"), (print_age, 25)]

for (func, arg) in lst:
    func(arg)

print("3. closures")
# Closures are functions that retain the bindings of the free variables that exist when the function is defined, 
#   so that they can be used later when the function is invoked and the defining scope is no longer available.
# Closure maintains the state of the outer function which is returned for later use.

def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure = outer_func(10) # closure is a function that retains the state of outer_func
print(closure) # 

print(closure(5)) # 15

print("4. Function Introspection")
# functions are objects, they can be processed with usual object tools
def func(x):
    return x

print(func("Calling the function")) # calling a function is one of python defined operations to work on function objects

# Other operations include:
print(f"Inspect the function name: {func.__name__}")
print(f"Function attr using dir: {dir(func)}")

# Function attributes are used to manage functions e.g. argument validation in decorators

print("5. user-defined function attributes")
# define a function
def user_defined_func(x):
    return x

print(user_defined_func("Call simply")) # call function
user_defined_func.count = 0 # add an attribute to the function
print(user_defined_func.count) # 
print(dir(user_defined_func)) # list all attributes of the function
# python separated user-defined attributes from built-in attributes by following a convention of using double underscores for built-in attributes
# in that case, built-in comes first in the list of attributes followed by user-defined attributes alphabetically ordered.

def user_defined_func1(x): pass

print(len(dir(user_defined_func1))) # list all attributes of the function
print([x for x in dir(user_defined_func1) if not x.startswith("__")]) # list user-defined attributes only

# Function attrs are useful in adding state info instead of using global variables, nonlocal variables, or classes
# The advatage here is that attrs can be accessed and modified from outside the function or inside.

print("6. Function Annotations")
# Function annotations are arbitrary python expressions that are associated with various part of functions and are completely optional.
# Annotation is any information that is not part of the code itself and can be used by tools(error tester) or libraries and other developers.
# They describe info about arguments and return values of functions.

def func(a,b,c):
    return a + b + c

print(func(1,2,3)) # 6

# Annotations are added using colons after the argument name or return value
# They dont have any effect on the function itself, they are just metadata
# Annotations are stored in __annotations__ attribute of the function
def func(a: int, b: int, c: int) -> int:
    return a + b + c

print(func(1,2,3)) # 6, no effect on the function
# Annotations are collected in a dictionary
print(f"function annotation: {func.__annotations__}") # {'a': <class 'int'>, 'b': <class 'int'>, 'c': <class 'int'>, 'return': <class 'int'>}

# Gotchas: 
# 1. Annotations are not enforced by Python, they are just metadata but you can use tools to enforce them and type check.
#    Annotations were proposed to be used in type hinting in Python 3 in pep 3107
