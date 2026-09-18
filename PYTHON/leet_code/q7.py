"""
consecutive numbers with highest sum
"""

arr = [3,4,5,8,1,7,6,1,2]

k = 3

max_sum = sum(arr[:k])

for window in range(1,len(arr)):

    cur_window_sum = sum(arr)