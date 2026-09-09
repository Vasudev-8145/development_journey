"""
odd_even programme using class
"""

class OddEven:

    def solution(self,num):

        if num == 0:
            return("Zero")

        elif num%2==0:
            return ("Even")

        elif num%2!=0:
            return ("Odd")

odd_even_instance = OddEven()

print(odd_even_instance.solution(10))
print(odd_even_instance.solution(15))
print(odd_even_instance.solution(0))