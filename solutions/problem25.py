DIGITS = 1000

def fib(n, p, index):
    if len(str(n)) > DIGITS - 1:
        return index
    return fib(n + p, n, index + 1)

"""
    RecursionError: maximum recursion depth exceeded while getting the str of an object
"""

def fib():
    n = 0 
    p = 1
    index = 0
    while len(str(n)) < DIGITS:
        n, p, index = n + p, n, index + 1
    return index

print(fib())