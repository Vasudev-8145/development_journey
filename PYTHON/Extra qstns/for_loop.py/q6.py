"""
Find all prime numbers between 1 and 50.
"""

for n in range(2,51):

    for i in range(2,n):

        if n%i == 0:
            break

    else:
        print(n,end=" ")

