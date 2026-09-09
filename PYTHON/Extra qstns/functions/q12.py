"""
create a menu driven calculator using functions
"""

def calculator(num1,num2):

    print("Enter your operation 1.Addition,2.Substracion3.Multiplication,4.Division")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        print(num1+num2)

    elif choice == 2:
        print(num2-num1)

    elif choice == 3:
        print(num1*num2)

    elif choice == 4:
        print(num1/num2)

calculator(2,4)