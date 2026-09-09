

expenses = [12000,11000,15000,17000,16000,13000]
#             0      1    2     3     4     5

march_month_expense = expenses[2]
print(march_month_expense)


#update jan month expenses as 15000

expenses[0] = 15000
print(expenses)


#display elements one by one


print("using index ____________")
for i in range(0,len(expenses)):
    print(expenses[i])

print("using in _____________________")
for amount in expenses:
    print(amount)