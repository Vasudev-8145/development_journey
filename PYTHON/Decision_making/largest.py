#largest among 3 numbers

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
if num1>num2 and num1>num3:
    print("num1 is largest")
elif num2>num3 and num2>num1:
    print("num2 is largest")
elif num3>num1 and num3>num2:
    print("num3 is largest")
else:
    print("3 numbers are equal")