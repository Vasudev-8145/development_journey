status_code_num = int(input("Enter status code 1/2/3/4:"))

match status_code_num:

    case 1:
        print("Success")

    case 2:
        print("Redirect")

    case 3:
        print("Client error")

    case 4:
        print("Server error")

    case _:
        print("Invalid code")