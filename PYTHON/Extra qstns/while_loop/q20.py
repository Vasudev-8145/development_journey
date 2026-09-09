"""
keep asking for apassword until its correct
"""

org_pass = 8145
user_pass = int(input("Enter 4 digit password:"))
count = 1

while user_pass != org_pass:

    user_pass = int(input("Enter 4 digit password:"))
    count+=1

if user_pass == org_pass:

    print("Login successfull!!")
    print("NUmber of attempts =",count)