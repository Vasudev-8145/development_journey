"""

      *      => row6  space=6 col=1
     * *     => row5  space=5 col=2 
    * * *    => row4  space=4 col=3 
   * * * *   => row3  space=3 col=4 
  * * * * *  => row2  space=2 col=5 
 * * * * * * => row1  space=1 col=6 

"""

for r in range(6,0,-1):

    for s in range(1,r+1):

        print(" ",end="")

    for c in range(1,(7-r)+1):

        print("*",end=" ")

    print()