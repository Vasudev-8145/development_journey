"""
print a right triangle pattern
"""

def right_triangle():

    for r in range(5,0,-1):

        for s in range(1,(r-1)+1):

            print(" ",end="")

        for c in range(1,(6-r)+1):
            print("*",end="")


        print()

right_triangle()