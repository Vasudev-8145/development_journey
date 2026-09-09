#(year not divisible by 100 amd divisible by 4) or (year divisible by 100 amd divisible by 400)
#leap year programme

year=int(input("Enter a year:"))
is_leap=(year%100!=0 and year%4==0) or (year%100==0 and year%400==0)
print(is_leap)