"""
define a function product that return product of all numbers
"""

def product(*args):

    result = 1

    for i in args:

        result *= i

    return result

print(product(10,20))
print(product(10,20,30))
