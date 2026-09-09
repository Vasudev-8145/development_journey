"""
placement count case study
"""

placement = [10,15,22,9,17,18]
#             0  1  2 3  4  5

# display feb month placement count

print(f"feb month placement count = {placement[1]}")

# update jan month placement count as 12

placement[0] = 12
print(f"updated placement count = {placement}")

# display placement counts where count>15

print("placement count>15")
for count in placement:

    if count>15:
        print(count)

# display highest placement without using max()

highest = placement[0]

for count in placement:

    if count>highest:
        highest = count

print(f"highest placement count = {highest}")

# display lowest placement without using min()

lowest = placement[0]

for i in placement:

    if i<lowest:
        lowest = i

print(f"lowest placement count = {lowest}")



