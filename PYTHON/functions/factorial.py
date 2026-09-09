"""
factorial of a number
"""

def factorial(num):

    fact = 1

    for i in range(1,num+1):

        fact = fact*i
        
    print(f"factorial of {num} = {fact}")

factorial(5)
factorial(7)