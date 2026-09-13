"""
python has a lambda keyword that allows you to create small anonymous functions in addition to the normal functions defined with the def keyword.

Lambda functions are syntactically restricted to a single expression. 

They can be used wherever function objects are required. 

They are often used in conjunction with typical functional concepts like filter(), map() and reduce().

lambda function are know as anonymous functions because they return a function object without assigning it to a variable.

They are used for inline function definition and execution deference until later.

syntax: lambda arguments: expression using the arguments
"""

# using def keyword
def add(x, y):
    return x + y

print(add(2, 3))

# defining the same function using lambda, have no name unless assigned to a variable
add1 = lambda x, y: x + y
print(add1(2, 3))
print(add1) # 

# why use lambda?
    # function shorthand for simple operations, they are defined in place and not assigned to a variable
    # instances where you need a simple function for a short period of time
    # 1. using lambda with filter, map and reduce functions
    # 2. using lambda with sorted function
    # 3. In callback handlers, they require a inline function definition
    # 4. In jump/action tables, they are used to define a list or a dictionary of functions

# Example: 
print("1. Action tables")
L = [lambda x: x ** 2, 
     lambda x: x ** 3, 
     lambda x: x ** 4]

for f in L:
    print(f(2))

print(L[0](3))

print("2. Multiway branch switching using lambda")
key = 'got'
actions = {'already': (lambda: 2 + 2),
 'got': (lambda: 2 * 4),
 'one': (lambda: 2 ** 6)}

print(actions[key]())


# Nesting lambdas
print("3. Nesting lambdas inside defs")
def action(x):
    return lambda y: x + y

print(action)

act = action(99)
print(act(2))

# we can nest lambdas inside other lambdas but should be a
print("4. Nesting lambdas inside lambdas")
action = (lambda x: (lambda y: x + y))
act = action(99)
print(act)
print(act(2))


# while def function can work in the same way, lambda is more concise and inline, their proximity to the code that uses them makes them easier to understand.
# def would require separate function barried deep incase of huge codebase.
# with lambda you can minimize the number of names in your code, making it more readable and clash free.
# lambda is a tool for creating functions on the fly, not for naming them, create when needed and have no unecessary reference to them.

# Gotchas of lambda
# 1. lambda is a single expression, not a block of statements, it is designed for simple functions
# 2. You as last resort, if you find yourself trying to do too much in a lambda, consider using a def instead.
#    lambda functions can obsfuscate the code and make it harder to understand.(simple is better than complex remember)


