"""
w.a function for common_divisors_of_two_number(num1,num2)
"""

def common_divisors(num1,num2):

    for i in range(1,min(num1,num2)+1):

        if num1%i == 0 and num2%i == 0:
            print(i,end=" ")

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

common_divisors(num1,num2)
 



    