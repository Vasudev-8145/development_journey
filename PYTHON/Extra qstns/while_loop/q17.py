"""
print cubes from 1 to n
"""

num = int(input("Enter a number:"))
i = 0
count = 1

while count<=num:

    i+=1
    cube = i**3
    print(cube)
    count+=1