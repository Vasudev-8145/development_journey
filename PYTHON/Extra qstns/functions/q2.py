"""
create a function to find the factorial
"""

num = int(input("Enter a number:"))

def factorial():

    fact = 1

    for i in range(1,num+1):

        fact = fact*i

    print(f"factorial of {num} = {fact}")

factorial()