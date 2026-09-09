

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

operation = input("select operation + - * /:")

result = 0

try:

    if operation == "+":

        result = num2+num1
    

    elif operation == "-":

        result = num1-num2
    

    elif operation == "*":

        result = num1*num2
    

    elif operation == "/":
            
        result = num1/num2

    else:
        print("Invalid")

except Exception as e:
    print(e)

else:
    print(result)