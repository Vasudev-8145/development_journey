"""

 * * * * * *  =>row=6 space=1 col=6
  * * * * *   =>row=5 space=2 col=5
   * * * *    =>row=4 space=3 col=4
    * * *     =>row=3 space=4 col=3
     * *      =>row=2 space=5 col=2
      *       =>row=1 space=6 col=1 
"""


for r in range(6,0,-1):

    for s in range(1,(7-r)+1):

        print(" ",end="")

    for c in range(1,r+1):

        print("*",end=" ")

    print()