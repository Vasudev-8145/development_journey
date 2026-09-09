"""
second highest placement count without using sorted()
"""


placement = [10,15,22,9,17,18]
#             0  1  2 3  4  5


first_max,second_max = 0,0

for count in placement:

    if count>first_max:

        second_max = first_max
        first_max = count

    elif count>second_max:

        second_max = count

print(f"second highest = {second_max}")


