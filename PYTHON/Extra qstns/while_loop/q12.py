"""
print the multiplication table of a given number
"""

num = int(input("Enter a number:"))
mul = 1

while mul<=10:

    res = mul*num
    print(f"{mul}*{num} = {res}")
    mul+=1
    