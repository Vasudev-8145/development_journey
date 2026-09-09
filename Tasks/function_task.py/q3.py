"""
w.a function for is_armstrong_number(number)
"""

def armstrong(num):

    org_num = num
    sum = 0
    count = len(str(num))

    while num!=0:

        digit = num%10
        exponent =  digit**count
        sum = sum+exponent
        num = num//10

    if sum == org_num:
        print(True)

    else:
        print(False)

num = int(input("Enter a number:"))

armstrong(num)