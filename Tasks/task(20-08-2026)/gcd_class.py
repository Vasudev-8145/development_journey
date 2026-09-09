"""
gcd of two number programme using class
"""

class Gcd:

    def solution(self,num1,num2):

        gcd = 1

        for i in range(1,min(num1,num2)+1):

            if num1%i == 0 and num2%i == 0:

                gcd = i

        print(f"GCD of {num1} and {num2} = {gcd}")

gcd_instance = Gcd()

gcd_instance.solution(8,16)
gcd_instance.solution(10,100)

