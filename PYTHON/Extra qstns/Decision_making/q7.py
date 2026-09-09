"""
Simple ATM: check balance, allow withdrawal only if sufficient.
"""

balance=5000
print("Your current balance is Rs.",balance)
withdraw_amnt=float(input("Enter withdrawal amount:"))
if withdraw_amnt<=balance:
    print("Withdrawal successfull")
    rem_balance=balance-withdraw_amnt
    print("Remaining balance is Rs.",rem_balance)
else:
    print("Insufficient balance!")
