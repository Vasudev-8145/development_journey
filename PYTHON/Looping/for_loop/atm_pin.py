"""
atm pin unlock
"""

atm_pin = 8145

for i in range(1,4):

    pin = int(input("Enter atm pin (max 3 attempts):"))

    if pin == atm_pin:
        print("You can continue your transaction..")

        break

else:
    print("Transaction blocked")