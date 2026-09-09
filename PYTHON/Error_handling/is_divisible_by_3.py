"""
is divisible by three
"""

def is_divisible_by_3(num):

    result = True

    if num%3 == 0:
        result = True

    else:
        result = False

    return result

assert is_divisible_by_3(9) == True,"test case 1 failed"
assert is_divisible_by_3(16) == False,"test case 2 failed"

