

from mysql import connector

class TicketCreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        if user==None and password==None:
            raise Exception("username and password required")

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="customer_support_db"
        )

        self.cursor = self.connection.cursor()
        

    def post(self,**kwargs):

        db_cols = ("customername","email","subject","description","category","priority","status","assignedto")

        difference = set(db_cols).difference(kwargs.keys())

        if difference:
            raise Exception(f"{difference} required")

        col_str = ",".join(db_cols)

        query = f"insert into supportticket ({col_str} values(%s,%s,%s,%s,%s,%s,%s,%s)"

        values = list(kwargs.keys())

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Record inserted....")

    def get(self):

        query = "select * from supportticket"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for i in records:
            print(i)

    def retrieve(self,id=None):

        query = "select * from supportticket where id=%s"

        values = (id,)

        self.cursor.execute(query,values)

        records = self.cursor.fetchone()

        print(records)

    def put(self,id=None,**kwargs):

        place_holder = ""

        for k in kwargs.keys():

            place_holder+=k+"=%s,"

        place_holder = place_holder.rstrip(",")

        query = f"update supportticket set {place_holder} where id=%s"

        values = list(kwargs.values())

        values.append(id)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Record updated...")

    def filter(self,**kwargs):

        place_holder = ""

        for k in kwargs.keys():

            place_holder += k+"=%s and "

        place_holder = place_holder.rstrip("and ")

        query = f"select * from supportticket where {place_holder}"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        records = self.cursor.fetchall()

        if records:
            print(records)

        else:
            print("No such records..")

    def summary(self):

        status_summary_query = "select status,count(*) from supportticket group by status"

        self.cursor.execute(status_summary_query)

        status_summary = self.cursor.fetchall()

        print(status_summary)

        priority_summary_query = "select priority,count(*) from supportticket group by priority"
        
        self.cursor.execute(priority_summary_query)
        
        priority_summary = self.cursor.fetchall()
        
        print(priority_summary)

    def delete(self,id=None):

        query = "delete from supportticket where id=%s"

        values=(id,)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Record deleted...")

ticket = TicketCreateListRetrieveUpdateDelete(user="root",password="Password@123")

# ticket.post(
#     customername="AJP",
#     email="alinjose@gmail.com",
#     subject="payment option not working",
#     description="My payment option is not working",
#     category="technical",
#     priority="urgent",
#     status="inprogress",
#     assignedto="Muhasina"
#     )

# ticket.get()

# ticket.retrieve(id=1)

# ticket.put(id=1,customername="varun",email="varun@gmail.com")

# ticket.delete(id=5)

# ticket.filter(status="open",priority="high")     

# ticket.summary()