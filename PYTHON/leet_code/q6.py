"""
find closest number to zero

arr = [-2,-3,1,2,3]
"""

arr = [-2,-3,1,2,3]

closest_num = arr[0]

for num in arr:

    if abs(num)<abs(closest_num):

        closest_num = num

if closest_num < 0 and abs(closest_num) in arr:

    print(abs(closest_num))

else:

    print(closest_num)