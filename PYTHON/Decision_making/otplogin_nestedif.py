"""
 Login System with Password and OTP

Task:
Ask for password.

If password is correct:

Ask for OTP

If OTP is correct → "Login successful"

Else → "Incorrect OTP"


Else → "Incorrect password"

"""

db_password = 8145

db_otp = 1234

password = int(input("Enter password:"))

if password == db_password:

    otp = int(input("Enter otp:"))

    if db_otp == otp:

        print("Login successfull")

    else:

        print("Invalid otp!!!")

else:

    print("Invalid password!!!")
