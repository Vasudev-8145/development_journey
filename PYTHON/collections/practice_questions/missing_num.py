"""
write a program to print least +ve missing number 

     arr=[1,2,4,5]
     o/p => 3

     eg2:
    arr=[1,3,4,5]
     o/p => 2
"""


arr = [1,2,4,5]

arr_sum = sum(arr)

total = 0

for num in range(0,(max(arr))+1):

    total += num

missing_num = total-arr_sum

print(missing_num)