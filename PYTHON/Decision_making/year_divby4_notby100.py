year=int(input("Enter year:"))
if year%100!=0 and year%4==0:
    print("year is not divisible by 100 and is divisible by 4")
else:
    print("year is divisible by 100 and is not divisible by 4")