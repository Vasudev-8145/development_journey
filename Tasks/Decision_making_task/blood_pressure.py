"""
Blood Pressure (Systolic)
- < 120: Normal
- 120 â€“ 129: Elevated
- 130 â€“ 139: High BP Stage 1
- â‰¥ 140: High BP Stage 2
"""

blood_pr = int(input("Enter your blood pressure:"))

if blood_pr<120:

    print("Normal")

elif blood_pr<130:

    print("Elavated")

elif blood_pr<140:

    print("High BP stage 1")

else:

    print("High BP stage 2")