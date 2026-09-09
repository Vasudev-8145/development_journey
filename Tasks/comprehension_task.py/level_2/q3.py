"""
Extract positive numbers Input: numbers=[-10,15,-8,20,5,-2] Expected
    Output: [15,20,5]

"""

numbers = [-10,15,-8,20,5,-2]

positive_num = [num for num in numbers if num>0]
print(positive_num)