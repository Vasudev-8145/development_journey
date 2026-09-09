"""
create = post
list = get
detail = retrieve
update = put
delete = delete
"""

from mysql import connector

class ExpenseCreateListDetailUpdateDelete:

    def __init__(self,user=None,password=None):

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="tripwise_db"
        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):

        query = """
        insert into expense(trip,paid_by,amount,category) values(%s,%s,%s,%s)
    """
        values = list(kwargs.values())

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Record added")

    def get(self):

        query = "select * from expense"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for exp in records:
            print(exp)

    def retrieve(self,id=None):

        query = "select * from expense where id=%s"

        values = (id,)

        self.cursor.execute(query,values)

        record = self.cursor.fetchone()

        print(record)

    def put(self,id=None,**kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder+=k+"=%s,"

        place_holder = place_holder.rstrip(",")

        query = f"update expense set {place_holder} where id=%s"

        values = list(kwargs.values())
        values.append(id)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Record updated")

    def delete(self,id=None):

        query = "delete from expense where id=%s"

        values = (id,)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Record deleted")

exp_instance = ExpenseCreateListDetailUpdateDelete(user="root",password="Password@123")

# exp_instance.post(trip="kochi",paid_by="chaacha",amount=500,category="travel expense")
        
# exp_instance.get() 

# exp_instance.retrieve(id=3)

# exp_instance.put(id=3,paid_by="anna durai",category="ticket")

exp_instance.delete(id=1)