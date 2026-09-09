"""
Simple login: check username AND password match.
"""

username="vasu@2005"
password=8145
user_username=input("Enter username:")
user_password=int(input("Enter 4 digit password:"))
if user_username==username and user_password==password:
    print("Login successfull")
else:
    print("Unable to login") 