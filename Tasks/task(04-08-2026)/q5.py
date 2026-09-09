"""
Find the smallest element in a list.
"""

numbers = [2,5,6,3,1,8]

smallest = numbers[0]

for num in numbers:

    if num<smallest:
        smallest=num

print(smallest)
