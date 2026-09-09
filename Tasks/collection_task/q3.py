"""
attendance = ["p","p","a","a","o","o","h"]

    write a program to print attendance count

"""

attendance = ["p","p","a","a","o","o","h"]

attendance_set = set(attendance)
attendance_count = {}

for attendence_each in attendance_set:

    attendance_count[attendence_each] = attendance.count(attendence_each)

print(attendance_count)