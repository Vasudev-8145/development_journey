"""
Check if a year is a leap year.
"""

year=int(input("Enter year:"))
if (year%100!=0 and year%4==0) or (year%100==0 and year%400==0):
    print("Leap year!!!")
else:
    print("Not a leap year")