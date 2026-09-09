"""
find the average of n numbers
"""

ll_lim = int(input("Enter lower limit:"))
up_lim = int(input("Enter upper limit:"))
sum = 0
count = 0

for i in range(ll_lim,up_lim+1):

    sum = sum+i
    count+=1

average = sum//count
print(f"Average = {average}")