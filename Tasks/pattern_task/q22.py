"""
hollow diamond pattern
"""

for r in range(1,8):

    for c in range(1,8):

        if (r+c==5) or (r-c==3) or (r+c==11) or (c-r==3):
            print("* ",end="")

        else:
            print(" ",end=" ")

    print()