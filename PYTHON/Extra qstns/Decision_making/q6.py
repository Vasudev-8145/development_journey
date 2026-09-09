"""
Classify a triangle as equilateral, isosceles, or scalene.
"""

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a==b==c:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else:
    print("Scalene")