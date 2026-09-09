"""
 ATM Withdrawal

Task:
Ask for PIN.

If PIN is correct:

Ask for withdrawal amount

If amount ≤ balance → "Withdrawal successful"

Else → "Insufficient balance"

Else → "Incorrect PIN"
"""

db_pin = 8145

balance = 5000

pin = int(input("Enter pin:"))

if pin == db_pin:

    amount = int(input("Enter withdrawal amount:"))

    if amount <= balance:
         
        print("Transaction successfull")

        rem_balance = balance-amount

        print("Remaining balance is Rs.",rem_balance)
    
    else:

        print("Inssuficient balance!!!!")

else:

    print("Invalid pin!!!")

