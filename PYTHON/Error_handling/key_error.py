

employee = {"id":100,"name":"ajp","dept":"hr"}

key = input("enter key:")

try:

    print(employee(key))

except Exception as e:
    print(e)

finally:

    print("db commit...")