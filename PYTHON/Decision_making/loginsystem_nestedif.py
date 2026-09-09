db_username = "messi"

db_password = 8145

username = input("Enter username:")

if username.lower() == db_username:

    password = int(input("Enter password:"))

    if password == db_password:

        print("LOGIN SUCCESSFULL")

    else:
        
        print("INVALID PASSWORD!!!")

else:

    print("INVALID USERNAME!!!")