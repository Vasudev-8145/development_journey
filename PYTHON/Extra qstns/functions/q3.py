"""
create a function to check wheather a number is prime
"""

num = int(input("Enter a number:"))

def prime():

    for i in range(2,num):

        if num%i == 0:
            print("Not a prime")
            break

    else:
        print("Prime number")

prime()