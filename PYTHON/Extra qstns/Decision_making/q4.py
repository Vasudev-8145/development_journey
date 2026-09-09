"""
Grade a student: A(>=90), B(>=80), C(>=70), D(>=60), F(<60).
"""

mark=int(input("Enter mark of the student:"))
if mark<60:
    print("Failed")
elif mark<70:
    print("D grade")
elif mark<80:
    print("C grade")
elif mark<90:
    print("B grade")
elif mark>=90 and mark<=100:
    print("A grade")