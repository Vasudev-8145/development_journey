"""
print a pyramid
"""

for r in range(6,0,-1):

    for s in range(1,r+1):

        print(" ",end="")

    for c in range(1,(7-r)+1):

        print("*",end=" ")

    print()