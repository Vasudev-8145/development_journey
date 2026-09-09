"""
write a program to print unique numbers 

        arr=[10,1,15,16,11,10,12,11]

        o/p => [1,15,16,12]
"""


arr = [10,1,15,16,11,10,12,11]

unique = set()

for num in arr:

    if arr.count(num) == 1:
        unique.add(num)

print(unique)

