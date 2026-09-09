num=int(input("Enter a number:"))
if num%100==0 and num%400==0:
    print("Number is divisible by both 100 and 400")
else:
    print("Number is not divisible by both 100 and 400")