"""
print squares from 1 to n
"""

num = int(input("Enter a number:"))
i = 0
count = 1

while count<=num:

    i+=1
    square = i**2
    print(square)
    count+=1
