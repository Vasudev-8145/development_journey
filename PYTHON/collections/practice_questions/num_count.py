"""
dictionary with num and its count
"""

arr = [10,1,15,16,11,12,10,11]

arr_set = set(arr)
num_count = {}

for num in arr:

    num_count[num] = arr.count(num)

print(num_count)