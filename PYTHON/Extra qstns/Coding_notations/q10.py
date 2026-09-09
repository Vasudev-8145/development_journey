"""
Write a student grade system with fully proper naming.
"""

pass_mark=50
student_name=input("Enter student name:")
student_mark=int(input("Enter student mark:"))
if student_mark>=pass_mark:
    print(f"{student_name} has passes the exam!")
else:
    print(f"{student_name} failed the exam!")