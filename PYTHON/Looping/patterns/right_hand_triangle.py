"""

      *   => row6 6space 1col   
     **   => row5 5space 2col
    ***   => row4 4space 3col
   ****   => row3 3space 4col
  *****   => row2 2space 5col
 ******   => row1 1space 6col
"""


for r in range(6,0,-1):

    for s in range(1,r+1):

        print(" ",end="")

    for c in range(1,(7-r)+1):

        print("*",end="")

    print()

