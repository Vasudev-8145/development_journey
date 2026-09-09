

from mysql import connector

class HospitalCreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        if user==None and password==None:
            raise Exception("Username and password required")

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="hospital_register_db"
        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):

        db_cols = ("patient_name","age","appoinment_status","treatment_status","doctor_name")

        difference = set(db_cols).difference(kwargs.keys())

        if difference:
            raise Exception(f"{difference} is missing")

        col_str = ",".join(db_cols)

        query = f"insert into patient_list({col_str}) values(%s,%s,%s,%s,%s)"

        values = list(kwargs.values())

        self.cursor.execute(query,values)
        self.connection.commit()

        print("Record inserted....")

    def get(self):

        query = "select * from patient_list"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for i in records:
            print(i)

    def retrieve(self,patient_name=None,doctor_name=None):

        query = "select * from patient_list where patient_name=%s or doctor_name=%s"

        values = (patient_name,doctor_name)

        self.cursor.execute(query,values)

        records = self.cursor.fetchone()

        print(records)

    def put(self,id=None,**kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder += k+"=%s,"

        place_holder = place_holder.rstrip(",")

        query = f"update patient_list set {place_holder} where id=%s"

        values = list(kwargs.values())
        values.append(id)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Record updated...")

    def filter(self,**kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder += k+"=%s or "

        place_holder = place_holder.rstrip("or ")

        query = f"select * from patient_list where {place_holder}"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        records = self.cursor.fetchall()

        if records:
            print(records)

        else:
            print("No such records")

    def summary(self):

        status_summary_query = "select appoinment_status,count(*) from patient_list group by appoinment_status"
        self.cursor.execute(status_summary_query)
        status_summary = self.cursor.fetchall()
        print(status_summary)

        doctor_summary_query = "select doctor_name,count(*) from patient_list group by doctor_name"
        self.cursor.execute(doctor_summary_query)
        doctor_summary = self.cursor.fetchall()
        print(doctor_summary)

    def delete(self,id=None):

        query = "delete from patient_list where id=%s"

        values = (id,)

        self.cursor.execute(query,values)
        self.connection.commit()

        print("Record deleted....")

hospital_instance = HospitalCreateListRetrieveUpdateDelete(user="root",password="Password@123")
    
# hospital_instance.post(patient_name="vasudev",age=21,appoinment_status="completed",treatment_status="completed",doctor_name="DR Anandhu unni")

# hospital_instance.get()

# hospital_instance.retrieve(patient_name="ajna")

# hospital_instance.put(id=1,appoinment_status="waiting",doctor_name="DR Anumol")

# hospital_instance.filter(appoinment_status="waiting",age=21)

# hospital_instance.summary()

# hospital_instance.delete(id=8)