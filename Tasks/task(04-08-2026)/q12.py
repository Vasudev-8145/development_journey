"""
Find all prime numbers in a list.
"""

numbers = [1,4,5,8,10,11]

for num in numbers:

    for i in range(2,num):

        if num%i == 0:
            break

    else:
        print(num)

