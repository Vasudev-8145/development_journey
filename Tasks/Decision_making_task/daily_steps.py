"""
Daily Steps
- < 5000: Sedentary
- 5000 â€“ 9999: Moderately Active
- â‰¥ 10000: Active

"""


daily_steps = int(input("Enter your daily steps:"))

if daily_steps<5000:

    print("sedentary")

elif daily_steps<10000:

    print("Moderate active")

elif daily_steps>=10000:

    print("active")

else:

    print("Invalid")