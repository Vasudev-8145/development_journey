#year not divisible by 100 and divisible by 4(non centuary leap year)

year=int(input("Enter year:"))
condition=year%100!=0 and year%4==0
print(condition)