"""
print a diamond pattern
"""

for r1 in range(4,0,-1):

    for s1 in range(1,(r1-1)+1):
        print(" ",end="")

    for c1 in range(1,(5-r1)+1):
        print("*",end=" ")   

    print()

for r2 in range(3,0,-1):

    for s2 in range(1,(4-r2)+1):
        print(" ",end="")

    for c2 in range(1,r2+1):
        print("*",end=" ")

    print()