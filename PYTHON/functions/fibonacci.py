"""
fibonacci series
sum of previous 2 numbers
"""

def fibonacci(num):

    first = 0
    second = 1

    for i in range(1,num+1):

        print(first,end=" ")
        next = first+second
        first = second
        second = next


fibonacci(10)
