"""
create a function with common_divisors_of_n with parameter number that will display common divisors of n
"""

def common_divisors_of_n(num):

    for i in range(1,num+1):

        if num%i == 0:
            print(i,end=" ")

common_divisors_of_n(10)