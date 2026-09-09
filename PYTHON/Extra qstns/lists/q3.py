"""
find the average
"""

numbers = [1,2,3,4,5]

average = 0
sum = 0

for num in numbers:

    sum += num
    average = sum//len(numbers)

print(average)