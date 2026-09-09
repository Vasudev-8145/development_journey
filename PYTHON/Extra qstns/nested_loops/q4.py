"""
find the sum of prime numbers
"""

ll_lim = int(input("Enter lower limit:"))
up_lim = int(input("Enter upper limit:"))
sum = 0

for num in range(ll_lim,up_lim+1):

    for i in range(2,num):

        if num%i == 0:
            break
    
    else:
        sum = sum+num

print(f"Sum of prime numbers = {sum}")