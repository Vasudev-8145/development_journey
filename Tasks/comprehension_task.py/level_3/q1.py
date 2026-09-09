"""
 Replace odd numbers with "Odd" Input:[2,5,8,7,10]
Output:[2,"Odd",8,"Odd",10]
"""

numbers = [2,5,8,7,10]

new_numbers = ["odd" if num%2!=0 else num for num in numbers ]
print(new_numbers)