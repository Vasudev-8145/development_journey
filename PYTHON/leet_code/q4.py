"""
two pair sum

arr = [2,3,4,5,6]
target:9
"""

arr = [2,3,4,5,6]
target = 9

for ch in arr:

    difference = target-ch

    if difference in arr:
        print(f"two pairs are {difference},{ch}")
        break