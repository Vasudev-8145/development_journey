"""
Stress Level (1-10)
- 1 â€“ 3: Low Stress
- 4 â€“ 6: Moderate Stress
- 7 â€“ 10: High Stress

"""

stress_level = int(input("Enter your stress level:"))

if stress_level<4:

    print("Low stress")

elif stress_level<7:

    print("Moderate stress")

elif stress_level<=10:

    print("High stress")

else:

    print("Invalid")