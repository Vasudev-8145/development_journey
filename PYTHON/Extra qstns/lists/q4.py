"""
count even numbers and odd numbers
"""

numbers = [1,2,3,4,5]

even_count = 0
odd_count = 0

for num in numbers:

    if num%2 == 0:
        even_count+=1

    elif num%2 != 0:
        odd_count+=1

print(f"count of even numbers = {even_count}")
print(f"count of odd numbers = {odd_count}")