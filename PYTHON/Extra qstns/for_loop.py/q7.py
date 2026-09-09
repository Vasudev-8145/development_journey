"""
Print the Fibonacci series up to n terms.
"""

num = int(input("Enter a number:"))
first_num = 0
second_num = 1

for i in range(1,num):

    print(first_num)
    first_num = second_num
    third_num = first_num+second_num
    second_num = third_num
    