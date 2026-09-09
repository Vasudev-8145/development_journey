height_in_cm=int(input("Enter your height in cm:"))
weight_in_kg=int(input("Enter your weight in kg:"))
height_in_m=height_in_cm/100
bmi=weight_in_kg/height_in_m**2
print("Your BMi is",bmi)
if bmi<=19:
    print("Underweight")
elif bmi<=25:
    print("Normal")
elif bmi<=30:
    print("Overweight")
else:
    print("Obesse")