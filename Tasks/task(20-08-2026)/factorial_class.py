"""
factorial programme using class
"""

class Factorial:

    def solution(self,num):

        fact = 1

        for i in range(1,num+1):

            fact *= i

        return (f"factorial of {num} = {fact}")

factorial_instance = Factorial()

print(factorial_instance.solution(5))
print(factorial_instance.solution(10))