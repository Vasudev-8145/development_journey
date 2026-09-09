"""
factorial of a user input number
"""

num = int(input("Enter a number:"))
i = 1
fact = 1

while i<=num:

    fact = fact*i
    i+=1

print(f"factorial of {num} = {fact}")