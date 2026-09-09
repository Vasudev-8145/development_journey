

from  mysql import connector

class WorkshopCreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        if user==None and password==None:
            raise Exception("username and password required")

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="auto_service_db"
        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):

        db_cols = ("customer_name","vehicle_number","vehicle_model","issue_description","assigned_mechanic","status","estimated_cost","final_bill")

        difference = set(db_cols).difference(kwargs.keys())

        if difference:
            raise Exception(f"{difference} is missing")

        col_str = ",".join(db_cols)

        query = f"insert into job_cards ({col_str}) values(%s,%s,%s,%s,%s,%s,%s,%s)"

        values = list(kwargs.values())

        self.cursor.execute(query,values)
        self.connection.commit()

        print("Record inserted....")

    def get(self):

        query = "select * from job_cards"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for i in records:
            print(i)

    def retrieve(self,vehicle_number=None,customer_name=None):

        query = "select * from job_cards where vehicle_number=%s or customer_name=%s"

        Values = (vehicle_number,customer_name)

        self.cursor.execute(query,Values)

        records = self.cursor.fetchone()

        print(records)

    def put(self,id=None,**kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder+=k+"=%s,"

        place_holder = place_holder.rstrip(",")

        query = f"update job_cards set {place_holder} where id=%s"

        values = list(kwargs.values())
        values.append(id)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Record updated...")

    def filter(self,**kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder+=k+"=%s and "

        place_holder = place_holder.rstrip("and ")

        query = f"select * from job_cards where {place_holder}"

        values = list(kwargs.values())

        self.cursor.execute(query,values)
        records = self.cursor.fetchall()

        if records:
            print(records)

        else:
            print("No such records")

    def summary(self):

        revenue_summary_query = "select status,sum(final_bill) from job_cards group by status"

        self.cursor.execute(revenue_summary_query)

        revenue_summary = self.cursor.fetchall()

        print(revenue_summary)

    def delete(self,id=None):

        query = "delete from job_cards where id=%s"

        values = (id,)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Record deleted...")


work_instance = WorkshopCreateListRetrieveUpdateDelete(user="root",password="Password@123")

# work_instance.post(customer_name = "haritha",vehicle_number="KL13L1728",vehicle_model="scooter",issue_description="engine work",assigned_mechanic="anupama",status="completed",estimated_cost=5000,final_bill=4500)

# work_instance.get()

# work_instance.retrieve(vehicle_number="KL13L1728")

# work_instance.put(id=2,status="delivered",final_bill=2000)

# work_instance.filter(assigned_mechanic="anupama")

# work_instance.summary()

# work_instance.delete(id=1)