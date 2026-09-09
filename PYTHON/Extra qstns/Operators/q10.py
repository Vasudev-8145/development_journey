"""
Build a calculator with all 4 basic operations using input.
"""

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("select from choice 1.Addition 2.Subtraction 3.Multiplication 4.Division")
choice=int(input("Enter choice number:"))
if choice==1:
    result=num1+num2
    print(num1,"+",num2,"=",result)
elif choice==2:
    result=num1-num2
    print(num1,"-",num2,"=",result)
elif choice==3:
    result=num1*num2
    print(num1,"*",num2,"=",result)
elif choice==4:
    result=num1/num2
    print(num1,"/",num2,"=",result)
else:
    print("invalid choice!!")
    