'''
Python provides a number of tools to support functional programming. 
These functional tools apply functions to sequences and other iterables automatically.
These include:

1. map() function: 
    - applies a function to each item in an iterable (list, tuple, etc.) and returns a list of the results.
    - syntax: map(function, iterable)
    - function: a function to apply to each item in the iterable
    - iterable: a sequence, collection or an iterator object
2. filter() function:
    - applies a function to each item in an iterable and returns a list of items for which the function returns True.
    - syntax: filter(function, iterable)
    - function: a function that returns True or False
    - iterable: a sequence, collection or an iterator object
3. reduce() function:
    - applies a function to pairs of items and returns a single result.
    - syntax: reduce(function, iterable)
    - function: a function that takes two arguments
    - iterable: a sequence, collection or an iterator object

    Other functional tools include:
    - list comprehensions: they are used to build lists by applying an expression to each item in a sequence
    - generator expressions: they are used to build generators by applying an expression to each item in a sequence
    - closures: they are used to retain the state of the outer function which is returned for later use
    - decorators: they are used to modify or extend functions or methods

'''

# 1. The map() function

# map() applies a function to each item in an iterable (list, tuple, etc.) and returns a list of the results.
# syntax: map(function, iterable)
# example, selecting columns in database tables, incremeting pay fields, etc.

# Example: updating all the counters in a list

# using for loop
counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10)

print("Using for loop")
print(updated)

# using map function
def inc(x): return x + 5
print("Using map function")
print(list(map(inc, counters))) # map returns an iterator, so we convert it to a list

# using map with lambda. This example is a greate candidate for lambda
print("Using map with lambda")
print(list(map(lambda x: x + 20, counters)))

# mapping is not limited to one argument or one iterable
print("Mapping multiple arguments")
print(list(map(lambda x, y: x + y, [1, 2, 3], [4, 5,6]))) 
# map pics a value from each iterable and passes them to the function
# if the iterables are of different lengths, map stops when the shortest iterable is exhausted
print(list(map(lambda x, y: x + y, [1, 2, 3], [4, 5])))

# Note
# map is a built-in function in Python 3 and returns an iterator, results are generated on demand. makes it memory efficient
# i.e. map is a generator function, it is not a list, so we convert it to a list to see the results
# map is a functional alternative to list comprehensions if the function is already defined and results are needed one at a time


# 2. The filter() function
# filter() applies a function to each item in an iterable and returns a list of items for which the function returns True.
# can be emulated with list comprehensions but filter is more readable and efficient

# syntax: filter(test_function, iterable)
# test_function: a function that returns True or False
# iterable: a sequence, collection or an iterator object

# picks item greater than zero
lst = list(range(-5, 5))
print(lst)
print("Filtering positive numbers")
print(list(filter(lambda x: x > 0, lst)))

# 3. The reduce() function
# reduce() applies a function to pairs of items and returns a single result.
# reduce is not a built-in function in Python 3, it is in the functools module
# it was moved to functools module in Python 3 because it is not as commonly used as map and filter plus list comprehensions and loops are more readable
# Also inbuilt sum(), min(), max() functions can be used to replace reduce

# syntax: reduce(function, iterable)

from functools import reduce
print("Using reduce function")
print(reduce(lambda x, y: x + y, [1, 2, 3, 4])) # 10
