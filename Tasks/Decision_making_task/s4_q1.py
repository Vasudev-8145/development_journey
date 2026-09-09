"""
Positive Number â€“ Even or Odd**
   - Check if positive. If yes, check for even/odd. Else, state "Not a positive number."

"""

num = int(input("Enter a number:"))

if num>0:

    if num%2 == 0:

        print("Number is even")

    else:

        print("Number is odd")

else:

    print("Number is not positive!!!Enter a positive number")