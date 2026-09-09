"""
Find the largest element in a list.
"""

numbers = [2,5,6,3,8]

largest = numbers[0]

for num in numbers:

    if num>largest:
        largest = num

print(largest)