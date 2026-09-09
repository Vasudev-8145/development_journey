num1 = int(input("Enter number1:"))

num2 = int(input("Enter number2:"))

option = input("Enter option min/max:")

match option:

    case "min":

        if num1<num2:

            print("Minimum is",num1)

        else:

            print("Minimum is",num2)

    case "max":

        if num1>num2:

            print("Maximum is",num1)

        else:

            print("Maximum is",num2)

    case _:

        print("Invalid option")