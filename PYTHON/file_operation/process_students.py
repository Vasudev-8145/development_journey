

fr_all = open("file_operation\\all_students.txt","r")
fr_passed = open("file_operation\\passed_students.txt","r")
fw_failed = open("file_operation\\failed_students.txt","w")

all_students = {name.rstrip("\n") for name in fr_all}

passed_students = {name.rstrip("\n") for name in fr_passed}

failed_students = all_students.difference(passed_students)

for students in failed_students:

    fw_failed.write(students+"\n")

print("completed...")
