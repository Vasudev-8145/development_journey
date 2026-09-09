"""
BMI calculator with categories (Underweight/Normal/Overweight/Obese).
"""

weight=float(input("Enter your weight:"))
height=float(input("Enter your height:"))
height_in_m=height/100
bmi=weight/(height_in_m**2)
print("Your BMI is",bmi)
if bmi<18.5:
    print("Underweight")
elif bmi<=25:
    print("Normal weight")
elif bmi<=30:
    print("Overweight")
else:
    print("Obesse")