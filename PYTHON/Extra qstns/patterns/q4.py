"""
print numbers in triangle form
"""

def number_triangle():

    for r in range(1,6):

        for c in range(1,r+1):

            print(c,end=" ")

        print()

number_triangle()