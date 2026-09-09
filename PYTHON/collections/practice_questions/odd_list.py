"""
w.a.p create a new list that contain odd numbers 
"""

lst = [10,11,12,15,14,17,18]

odd_lst = []

for num in lst:

    if num%2!=0:
        odd_lst.append(num)

print(odd_lst)