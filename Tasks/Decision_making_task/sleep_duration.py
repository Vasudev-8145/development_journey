"""
Sleep Duration
- < 6: Sleep Deprived
- 6 â€“ 8: Healthy Sleep
- > 8: Oversleeping
"""

sleep_hr = int(input("Enter your sleeping hours:"))

if sleep_hr<6:

    print("sleep deprived")

elif sleep_hr<9:

    print("healthy sleep")

elif sleep_hr>8:

    print("oversleeping")

else:

    print("Invalid")