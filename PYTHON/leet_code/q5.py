"""
reverse a given list without using reverse and slicing

arr = [1,10,2,200,3,300]
"""

arr = [1,10,2,200,3,300]

reverse = []

for i in range(0,len(arr)):

    popped_element = arr.pop()
    reverse.append(popped_element)

print(reverse)