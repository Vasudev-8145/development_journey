"""
last divisor of a number other than same number
"""

def last_divisor(num):

    for i in range(num-1,1,-1):

        if num%i == 0:
            print(i)
            break

    else:
        print("No last divisor other than same number")

last_divisor(8)
last_divisor(10)
last_divisor(12)
last_divisor(7)