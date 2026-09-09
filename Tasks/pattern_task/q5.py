"""
number changing pyramid
"""

num = 1

for r in range(1,5):

    for c in range(1,r+1):

        print(num,end=" ")
        num+=1

    print()

