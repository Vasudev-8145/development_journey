"""
write a program to print least +ve missing number 

     arr=[1,2,4,5]
     o/p => 3

     eg2:
    arr=[1,3,4,5]
     o/p => 2
"""


arr = [1,2,4,5]

max_num = max(arr)
total = 0

for num in range(1,max_num+1):
    total +=num

arr_sum = sum(arr)

missing_num = total-arr_sum

print(missing_num)
