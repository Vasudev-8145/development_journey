"""
3 points lie on the same line
"""

x1,y1 = 10,8 #a

x2,y2 = 13,10 #b

x3,y3 = 16,12 #c

slope_ab = (y2-y1)/(x2-x1)

slope_bc = (y3-y2)/(x3-x2)

if slope_ab == slope_bc:

    print("points are on same line")

else:

    print("points are not in same line")