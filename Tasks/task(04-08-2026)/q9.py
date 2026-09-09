"""
Find all odd numbers in a list.
"""

numbers = [2,5,6,3,1,8]

odds = [num for num in numbers if num%2 != 0]

print(odds)