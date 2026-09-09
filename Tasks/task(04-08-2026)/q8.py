"""
Find all even numbers in a list.
"""

numbers = [2,5,6,3,1,8]

evens = [num for num in numbers if num%2 == 0]

print(evens)