"""
create a function to find maximum of two numbers
"""

def max_of_two(num1,num2):

    if num1 > num2:
        print(f"{num1} is greatest")

    elif num2 > num1:
        print(f"{num2} is greatest")

    else:
        print(f"{num1} and {num2} are equal")

max_of_two(2,5)
max_of_two(4,2)