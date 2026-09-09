"""
hollow reverse triangle pattern
"""

for r in range(1,6):

    for c in range(1,10):

        if (r-c==0) or (r+c==10) or (r==1 and c%2!=0):
            print("*",end="")

        else:
            print(" ",end="")

    print()