"""
is_fibonacci_number
"""

def is_fibonacci(num):

    first = 0
    second = 1
    next = 1

    if num == first or num == second:
        print(f"{num} is a fibonacci number")
        
    else:

        while next<=num:

            next = first+second
            first = second
            second = next

            if next == num:
                print(f"{num} is a fibonacci number")
                break

        else:
            print(f"{num} is not a fibonacci number")

is_fibonacci(0)
is_fibonacci(1)
is_fibonacci(24)
is_fibonacci(34)



