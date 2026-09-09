"""
Forming triangle with 3 angles
"""


angle1 = int(input("Enter frist angle:"))

angle2 = int(input("Enter second angle:"))

angle3 = int(input("Enter third angle:"))

if angle1>0 and angle2>0 and angle3>0:

    if angle1+angle2+angle3 == 180:

        print("Triangle can be formed")

    else:

        print("Triangle can't be formed!!Sum of angles must be 180 degree")

else:

    print("Triangle can't be formed!!An angle can't be zero")