"""
hollow hourglass pattern
"""

for r in range(1,8):

    for c in range(1,8):

        if (r==c) or (r+c==8) or (r==1 and c%2!=0) or (r==7 and c%2!=0):
            print("*",end=" ")

        else:
            print(" ",end=" ")

    print()