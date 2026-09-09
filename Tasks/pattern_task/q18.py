"""
reverse number triangle pattern
"""


for r in range(1,5):

    for c in range(1,8):

        if (r+c==2):
            print("1",end="")

        elif (r+c==4 and r!=3):
            print("2",end="")

        elif (r+c==6 and r!=4):
            print("3",end="")

        elif (r+c==8):
            print("4",end="")

        else:
            print(" ",end="")

    print()
        
        

  

