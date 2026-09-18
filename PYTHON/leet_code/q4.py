"""
two pair sum

arr = [2,3,4,5,6]
target:9
"""

# arr = [2,3,4,5,6]
# target = 9

# for ch in arr:

#     difference = target-ch

#     if difference in arr:
#         print(f"two pairs are {difference},{ch}")
#         break

"""
two pointer method
"""

arr = [1,4,2,3,7,6]
arr.sort()

target = 11
left = 0
right = len(arr)-1

while(left<right):

    cur_sum = arr[left]+arr[right]

    if cur_sum == target:

        print(arr[left],arr[right],"pair")
        break

    elif cur_sum > target:
        right = right-1

    elif cur_sum < target:
        left = left-1
