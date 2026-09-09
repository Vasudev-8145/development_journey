
# road_issue_db,
# issues [id,title,location,posted_by,status(unsolved,solved)]


from mysql import connector

class RoadIssueCreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="road_issue_db"
        )

        self.cursor=self.connection.cursor()

    def post(self,**kwargs):

        query = "insert into issues(title,location,posted_by,status) values(%s,%s,%s,%s)"

        values = list(kwargs.values())

        self.cursor.execute(query,values)
        self.connection.commit()

        print("Record added....")

    def get(self):

        query = "select * from issues"

        self.cursor.execute(query)
        records = self.cursor.fetchall()

        for i in records:
            print(i)

    def retrieve(self,id=None):

        query = "select * from issues where id=%s"

        values = (id,)

        self.cursor.execute(query,values)
        records = self.cursor.fetchone()

        print(records)

    def put(self,id=None,**kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder += k+"=%s,"

        place_holder = place_holder.rstrip(",")

        query = f"update issues set {place_holder} where id=%s"

        values = list(kwargs.values())
        values.append(id)

        self.cursor.execute(query,values)
        self.connection.commit()

        print("Record updated...")

    def delete(self,id=None):

        query = "delete from issues where id=%s"
        values = (id,)

        self.cursor.execute(query,values)
        self.connection.commit()

        print("Record deleted...")

road_instance = RoadIssueCreateListRetrieveUpdateDelete(user="root",password="Password@123")        

# road_instance.post(title="electricity line broken",location="ottappalam",posted_by="Haritha",status="unsolved")

# road_instance.get()

# road_instance.retrieve(id=1)

# road_instance.put(id=1,location="Round of thrissur",status="unsolved")

# road_instance.delete(id=1)