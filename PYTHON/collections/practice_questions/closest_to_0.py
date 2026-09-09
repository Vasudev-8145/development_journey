"""
print closest number to zero
"""

arr = [-3,-2,1,-1,2,3]

closest_num = arr[0]

for num in arr:

    if abs(num) < abs(closest_num):
        closest_num = num

    elif abs(num) == abs(closest_num) and num > closest_num:
        closest_num = num

print(closest_num)