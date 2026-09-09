"""
gcd of two numbers
"""

def gcd_of_two(num1,num2):

    gcd = 1

    for i in range(1,min(num1,num2)+1):

        if num1%i == 0 and num2%i == 0:
            gcd = i

    print(f"GCD = {gcd}")

gcd_of_two(24,18)
gcd_of_two(10,20)