"""
find product of all numbers in which upper limit and lower limit is given by the user
"""

up_lim = int(input("Enter upper limit:"))
low_lim = int(input("Enter lower limit:"))
product = 1

while low_lim<=up_lim:

    product = product*low_lim
    low_lim+=1

print(product)