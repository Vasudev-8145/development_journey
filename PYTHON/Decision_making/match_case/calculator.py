num1 = int(input("Enter number 1:"))

num2 = int(input("Enter number 2:"))

option = int(input("Enter a option 1.Addition 2.Subtraction 3.Multiplication 4.Division:"))

match option:

    case 1:
        print("Result =",num1+num2)

    case 2:
        print("Result =",num1-num2)

    case 3:
        print("Result =",num1*num2)

    case 4:
        print("Result =",num1/num2)

    case _:
        print("Invalid option")