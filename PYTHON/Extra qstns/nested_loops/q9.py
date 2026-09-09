"""
Find all 3-digit Armstrong numbers.
"""

for num in range(100,1000):

    org_num = num
    count = len(str(num))
    sum = 0

    while num!=0:

        digit = num%10
        exponent = digit**count
        sum = sum+exponent
        num = num//10

    if sum == org_num:
        print(org_num)

