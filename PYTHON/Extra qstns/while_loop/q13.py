"""
print the fibonacci series
"""

num = int(input("Enter a number:"))
first_num = 0
second_num = 1
count = 0

while count<=num:

    print(first_num)
    third_num = first_num+second_num
    first_num = second_num
    second_num = third_num
    count+=1