"""
Recursive are functions that call themselves either directly or indirectly in order to loop.

This functions allows us to traverse structures that have arbitrary and upredictable shape and depth e.g:
    - planning routes
    - analyzing language
    - crawling links on the web

Recursive functions can even be used as alternative to simple loops and iterations though they are not always the best choice in terms
of simplicity and performance.

"""

# Example 1: sumation of list. This a simple example of recursive function, loops would be more efficient saving memory and time
            # recursive functions requires fresh local scope for each call and also execution is slower than loops because of multiple function calls
print("Example 1") 
def sum_list(lst):
    if len(lst) == 0: # base case, when the list is empty, base case is important to avoid infinite loop by breaking the recursion
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
   
print(sum_list([1,2,3,4,5]))

# recursion using ternary operator
def sum_list_ternary_operator(l):
    return 0 if not l else l[0] + sum_list_ternary_operator(l[1:])

print(sum_list_ternary_operator([1,2,3,4,5]))


# we can have a type-agnostic summing functions as long as list elements support addition e.g. strings concatenation

def sum_list_type_agnostic1(l):
    if len(l)== 1: # base case, when the list has only one element
        return l[0]
    return l[0] + sum_list_type_agnostic1(l[1:])

print(sum_list_type_agnostic1(["k","e","l","v","i","n",]))


def sum_list_type_agnostic2(L):
    # print(f"Entry--> {L}")
    first, *rest = L
    print(f"rest--> {rest}")
    return first if not rest else first + sum_list_type_agnostic2(rest) # Use 3.X ext seq assign


print(sum_list_type_agnostic2([1,2,3,4,5]))
print(sum_list_type_agnostic2(["k","e","l","v","i","n","o"]))
print(sum_list_type_agnostic2("kefini"))

# Example 2: factorial
print("Example 2") 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
# However, recusion is best suited for arbitrary and unpredictable data structures.


# Example 3: sum of nested list
print("Example 3") 
lst = [1,[2,[3,4],5,6,[7,8]],9] # nested may take any shape and depth, very unpredictable. Loops can't cover all possibilities since they are arbitrary
# loops are not the best choice for this kind of structure because the depth of the list is unpredictable or this is
# ... not a linear list. Recursion is the best choice for this kind of structure

def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

print(sumtree(lst))


# Example 4: Looping versus recursion


# Example 5: Recursion verses queues and stacks
# - python performs recursion using stack, each function call is placed on the stack and popped off when the function returns
# - We can implement explicit stack or queue to simulate recursion and understand inner workings of recursion

# Example 5(a): first in first out (FIFO) queue also known as breadth-first search (BFS)
# - queue is a data structure that allows us to add and remove elements in a first-in-first-out manner
# - instead of issuing recursive calls, an item is added to the end of the queue and removed from the front
# - the list is processed level by level, breadth-first search (BFS).
# - this is a way of simulating recursion without using recursion
def sumtree_queue(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot

print(f"using queue: {sumtree_queue(lst)}")


# Example 5(b): last in first out (LIFO) stack also known as depth-first search (DFS)
# - This simulates traversal recursion closely, it simply pops an item and adds to the front of the stack
# - this is a way of simulating recursion without using recursion

def sumtree_stack(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front
    return tot 

# conclusion:
# 1. Why use recursion?
# Recursive are more natural compared to stack and queue, they are more readable and easier to write
# Recursion also automate the stack management, unless we have a good reason to do otherwise, we should use recursion
# Some programs may require FIFO queue, e.g:
"""
For example, in **web crawling**, pages are often assigned scores based on their content, 
and a FIFO queue ensures that pages are processed in the order they were discovered. 
This approach helps maintain a logical progression, ensuring that higher-level pages 
(such as homepages) are processed before their deeper links, leading to a more structured and efficient crawl.
"""

# 2. Dos and Don'ts of recursion
"""
Large recursion apps require critically thought out implimentation.
a. Avoid cycles & repeats: Recursion should not be used in a cycle or repeat, it will lead to infinite loop.
   - For simple cases like traversing a hierachical list, cycles isn't a problem.
   - For complex cases like cyclic graph data it is a problem. It would lead to infinite loop running out of call-stack space(stack overflow/ maximum recursion depth exceeded).
   - We can use a list,dictionary to keep track of visited nodes/ state to avoid cycles.

b. Record paths taken later use.
   - In some cases, we may need to record the path taken to reach a solution, we can use a list or dictionary to keep track of the path.
   - Python has default stack limit which can be extended using sys.setrecursionlimit(limit) but it is not recommended.
   - We can use a stack to keep track of the path taken.


c. Expand stack space instead of queus and stacks.
"""

print("Example 6: Stack overflow due to cycles and repeats")

# This is an example of a cyclic graph, it will lead to infinite loop
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def visit(node):
    print(node)
    for neighbor in graph[node]:
        visit(neighbor)

# visit('A')  # This will lead to infinite loop leading to a RecursionError: maximum recursion depth exceeded 

# To avoid cycles, we can use a list to keep track of visited nodes
def visit(node, visited=None):
    if visited is None: # initialize visited set for the first call
        visited = set()  # set is more efficient for membership testing and does not allow duplicates

    if node in visited: # this checks if the node has been visited before
        return
    
    print(node)
    visited.add(node) # add the node to the visited set so that we don't visit it again

    for neighbor in graph[node]:
        visit(neighbor, visited)

visit('A')