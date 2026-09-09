"""
Oxygen Level (SpO2)
- â‰¥ 95: Normal
- 90 â€“ 94: Mild Concern
- < 90: Critical
"""

oxygen_level = int(input("Enter your oxygen level:"))

if oxygen_level<90:

    print("critical")

elif oxygen_level<95:

    print("Mild concern")

elif oxygen_level>=95:

    print("Normal ")

else:

    print("Invalid")