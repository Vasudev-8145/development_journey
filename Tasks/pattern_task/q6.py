"""
zero one triangle
"""



for r in range(1,5):
    
    for c in range(1,r+1):

        if r==c or r-c==2:
            print("1",end=" ")

        elif r-c==1 or r-c==3:
            print("0",end=" ")

    print()
        




       