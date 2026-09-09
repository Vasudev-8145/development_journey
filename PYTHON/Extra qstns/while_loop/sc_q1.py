"""
1. ATM Withdrawal

A user has ₹10,000 in their account.

Keep asking for a withdrawal amount until the balance becomes 0 or the user enters 0 to stop.

Display the remaining balance after each successful withdrawal.

Do not allow withdrawals greater than the current balance.
"""

user_bal = 10000
withdrawal = int(input("Enter withdrawal amount (press 0 to stop):"))

while user_bal!=0 and withdrawal!=0:

    if withdrawal>user_bal:
        print("Insufficient balance !!")

    else:

        user_bal = user_bal-withdrawal
       
        print("Withdrawal successfull !!")
        print("Remaining balance =",user_bal)

    if user_bal!=0:
        withdrawal = int(input("Enter withdrawal amount (press 0 to stop):"))

print("Thank you !")
    