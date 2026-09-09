"""
food_logs
"""

"""
create|add = post
list|access all = get
detail = retrieve
update = put
remove = delete
"""

class DietLens:

    def __init__(self):

        self.food_logs = [
            {"id":1,"name":"dosa","calorie":180,"owner":"sourav"}
        ]

    def post(self,**kwargs):

        required_fields = {"id","name","calorie","owner"}

        missing_fields = required_fields.difference(kwargs.keys())

        if missing_fields:
            raise ValueError(missing_fields,"are missing") # raise exception pakaram raise valueerror

        self.food_logs.append(kwargs)

        print("Data has been added...!")

    def get(self):

        if len(self.food_logs)==0:
            print("No records found!!")

        else:
            for logs in self.food_logs:
                print(logs)

    def retrieve(self,id=None):

        if not id:
            raise ValueError("id missing")

        else:
            return [logs for logs in self.food_logs if logs.get("id")==id]

    def put(self,id=None,**kwargs):

        log = [logs for logs in self.food_logs if logs.get("id")==id][0]
        log.update(kwargs)
        print("Record has been updated...")
        print(log)

    def delete(self,id=None):

        log = [logs for logs in self.food_logs if logs.get("id")==id][0]

        self.food_logs.remove(log)
        print("Record deleted")
        self.get()
  
dietlens_instance = DietLens()
dietlens_instance.post(id=2,name="chappathi",calorie=150,owner="habeeb")
dietlens_instance.post(id=3,name="poratta",calorie=300,owner="sooraj")
# dietlens_instance.get()
# print(dietlens_instance.retrieve(id=2))
# dietlens_instance.put(id=1,name="Ghee rost",calorie=500)
# dietlens_instance.delete(id=2)