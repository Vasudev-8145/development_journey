"""
sum of n numbers with start and stop
"""

def sum_of_n(start,stop):

    sum = 0

    for i in range(start,stop+1):

        sum = sum+i

    print(sum)

sum_of_n(5,10)
sum_of_n(50,100)