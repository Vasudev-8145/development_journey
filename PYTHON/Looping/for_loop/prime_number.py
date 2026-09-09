"""
display first divisor of a number other than 1 and same number
display no divisor exist

OR

prime number
"""

num = int(input("Enter a number:"))

for i in range(2,num):

    if num%i == 0:
        print("not prime number")

        break

else:
    print("prime number")

"""
OR

step1: set is_prime as True
step2: input number
step3: repeat for i from 2 to number-1
    step4: chk if number%1==0 then
    step5: update is_prime as false then exist
step6: display is_prime
"""



