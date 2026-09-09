"""
Calculate the average of the numbers in a list.
"""

numbers = [2,5,6,3,1,8]

sum = 0
count = 0

for num in numbers:

    sum+=num
    count+=1

    average = sum/count

print(average)