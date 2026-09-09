"""
hollow butterfly star pattern
"""

for r in range(1,8):

    for c in range(1,8):

        if (r==c) or (r+c==8) or (r%2!=0 and c==1) or (r%2!=0 and c==7):

            print("*",end=" ")

        else:
            print(" ",end=" ")

    print()