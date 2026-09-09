"""
Display all numbers from 20 to 50 that are divisible by both 2 and 6
"""

num = 20

while (num<=50):

    if num%2 == 0 and num%6 == 0:
        print(num)

    num+=1