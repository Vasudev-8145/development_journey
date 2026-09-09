"""
pascals rigth triangle
"""


for r in range(1,8):

    for c in range(1,5):

        if (r==c) or (r+c==8) or (r==4 and c==2) or (c==1 and r%2!=0):
            print("*",end=" ")

        else:
            print(" ",end=" ")

    print()