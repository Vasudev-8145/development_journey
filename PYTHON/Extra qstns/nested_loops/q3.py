"""
count prime numbers from 1 to 50
"""

count = 0

for num in range(1,51):

    for i in range(2,num):

        if num%i == 0:
            break

    else:
        count+=1

print(f"Number of prime numbers = {count}")