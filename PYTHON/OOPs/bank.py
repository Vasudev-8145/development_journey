"""
bank details
"""

class Bank:

    acc_number:int
    balance:float
    ac_type:str
    customer_name:str

    def __init__(self,acc_number,balance,ac_type,customer_name):

        self.acc_number = acc_number
        self.balance = balance
        self.ac_type = ac_type
        self.customer_name = customer_name
        print("Your account is now visible")

    def deposit(self,amount):

        self.balance+=amount
        print(f"your account has been credited {amount} available balance = {self.balance}")

    def withdraw(self,amount):

        if amount > self.balance:
            raise Exception("Insufficient balance")

        else:
            self.balance-=amount
            print(f"your account has been debited {amount} available balance = {self.balance}")

    def get_balance(self):

        print(f"balance = {self.balance}")

customer1_instance = Bank(789456,500,"savings","messi")
customer1_instance.deposit(1500)
customer1_instance.withdraw(500)
customer1_instance.get_balance()


        