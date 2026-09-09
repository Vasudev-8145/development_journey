"""
fundwise user has to add,list,detail,update,delete his daily expense
each expense with id,title,amount,category,owner
"""

class Fundwise:

    def __init__(self):

        self.daily_expense = [
                    {"id":1,"title":"travel expense","amount":250,"category":"cash","owner":"messi"}
        ]

    def post(self,**kwargs):

        required_fields = {"id","title","amount","category","owner"}
        missing_fields = required_fields.difference(kwargs.keys())

        if missing_fields:
            raise ValueError(missing_fields,"are missing")

        self.daily_expense.append(kwargs)
        print("Record has been added")

    def get(self):

        if len(self.daily_expense)==0:
            print("No record found")

        else:
            for log in self.daily_expense:
                print(log)

    def retreive(self,id=None):

        if not id:
            raise ValueError("id missing")

        else:
            return [log for log in self.daily_expense if log.get("id")==id]

    def put(self,id=None,**kwargs):

        log = [fund for fund in self.daily_expense if fund.get("id")==id][0]

        log.update(kwargs)

        print("Record updated")
        print(log)

    def delete(self,id=None):

        log = [fund for fund in self.daily_expense if fund.get("id")==id][0]

        self.daily_expense.remove(log)

        print("Record deleted")

        self.get()

daily_expense_instance = Fundwise()

daily_expense_instance.post(id=2,title="food expense",amount=300,category="gpay",owner="ronaldo")
daily_expense_instance.post(id=3,title="grocery expense",amount=200,category="cash",owner="neymar")

# daily_expense_instance.get()

# print(daily_expense_instance.retreive(id=2))

# daily_expense_instance.put(id=2,category="card",owner="yamal")

# daily_expense_instance.delete(id=3)

        