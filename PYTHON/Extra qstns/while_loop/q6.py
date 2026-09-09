"""
find the factorial of a number
"""

num = int(input("Enter a number:"))
i = 1
fact = 1

while i<=num:

    fact = fact*i
    i+=1

print(fact)