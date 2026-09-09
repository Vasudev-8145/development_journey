"""
2. Online Shopping Cart

A customer keeps entering product prices.

Continue taking prices until the user enters -1.

Ignore prices less than or equal to 0 (except -1).

Find and print:

Total bill

Number of valid products

Average product price

"""

product_prize = int(input("Enter product prize (press -1 to stop):"))
total_bill = product_prize
count = 0

while product_prize!=-1 and product_prize>0:

    if product_prize<=0:
        print("Price cant be enterred")

    else:
        product_prize = int(input("Enter product prize (press -1 to stop):"))
        count+=1

        total_bill = total_bill+product_prize
        average = total_bill//count

        print(f"Total bill = {total_bill}")
        print(f"Number of valid products = {count}")
        print(f"Average product prize = {average}")

print("Thank you!")