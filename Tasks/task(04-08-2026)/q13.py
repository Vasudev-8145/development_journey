"""
Find all negative numbers in a list.
"""

numbers = [-5,1,-3,6,7,-2]

negatives = [num for num in numbers if num < 0]
print(negatives)