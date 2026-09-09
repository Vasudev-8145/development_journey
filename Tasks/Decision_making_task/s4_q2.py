"""
**Driving License Eligibility**
   - Age â‰¥ 18: Ask if test passed (yes/no).
   - Yes: "License Approved" | No: "Test not cleared."
   - Age < 18: "Not eligible due to age."

"""

age = int(input("Enter age:"))

if age>=18:

    test_passed = input("Did you pass the tes(yes/No):")

    if test_passed.lower() == "yes":

        print("License Approved!!")

    elif test_passed.lower() == "no":

        print("Test not cleared")

else:

    print("You are not eligible due to age")