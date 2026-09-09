"""
k pattern
"""


for r in range(1,8):

    for c in range(1,5):

        if (r==1) or (r==7) or (c==1) or (c==2 and r!=4) or (c==3 and r!=3 and r!=4 and r!=5):
            print("*",end=" ")

        else:
            print(" ",end=" ")

    print()