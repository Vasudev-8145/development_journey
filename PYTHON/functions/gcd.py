"""
gcd of a number is its last common divisor other than same number
"""

def gcd_of_num(num):

    for i in range(1,num):

        if num%i == 0:
            gcd = i

    print(gcd)

gcd_of_num(8)

