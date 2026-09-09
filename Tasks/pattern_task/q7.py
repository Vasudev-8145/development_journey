"""
palindrome triangular
"""

for r in range(1,5):

    for c in range(1,8):

        if c==4:
            print("1",end=" ")

        elif (c==3 or c==5) and r!=1:
            print("2",end=" ")

        elif (c==2 or c==6) and r!=1 and r!=2:
            print("3",end=" ")

        elif (r-c==3 or c-r==3) and r!=1 and r!=2 and r!=3:
            print("4",end=" ")

        else:
            print(" ",end=" ")

    print()
            