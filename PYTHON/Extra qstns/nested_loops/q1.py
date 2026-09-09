"""
print multiplication tables from 1 to 10
"""

mul = 0

for i in range(1,11):

    for j in range(1,11):

        mul = j*i
        print(f"{j} * {i} = {mul}")

        