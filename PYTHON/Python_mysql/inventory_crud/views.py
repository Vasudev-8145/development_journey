"""
Inventory Stock Management System
"""

from mysql import connector

class StockCreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        if user==None and password==None:
            raise Exception("username and password required")

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="inventory_db"
        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):

        db_cols = ("product_name","category","price","stock_quantity","supplier_name")

        difference = set(db_cols).difference(kwargs.keys())

        if difference:
            raise Exception(f"{difference} is missing")

        col_str = ",".join(db_cols)

        query = f"insert into products({col_str}) values(%s,%s,%s,%s,%S)"

        values = list(kwargs.values())

        self.cursor.execute(query,values)
        self.connection.commit()

        print("Record added....")

    def get(self):
    
        query = "select * from products"
    
        self.cursor.execute(query)
    
        records = self.cursor.fetchall()
    
        for i in records:
            print(i)
    
    def retrieve(self,id=None):
    
        query = "select * from product where id=%s"
    
        values = (id,)
    
        self.cursor.execute(query,values)
    
        records = self.cursor.fetchone()
    
        print(records)
    
    def put(self,id=None,**kwargs):
    
        place_holder = ""
    
        for k in kwargs.keys():
    
            place_holder+=k+"=%s,"
    
        place_holder = place_holder.rstrip(",")
    
        query = f"update product set {place_holder} where id=%s"
    
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
    
        query = f"select * from product where {place_holder}"
    
        values = list(kwargs.values())
    
        self.cursor.execute(query,values)
    
        records = self.cursor.fetchall()
    
        if records:
            print(records)
    
        else:
            print("No such records..")
    
        def summary(self):
    
            category_summary_query = "select category,count(*) from product group by category"
    
            self.cursor.execute(category_summary_query)
    
            category_summary = self.cursor.fetchall()
    
            print(category_summary)
    
            price_summary_query = "select price,count(*) from product group by price"
            
            self.cursor.execute(price_summary_query)
            
            price_summary = self.cursor.fetchall()
            
            print(price_summary)
    
    def delete(self,id=None):
    
        query = "delete from product where id=%s"
    
        values=(id,)
    
        self.cursor.execute(query,values)
    
        self.connection.commit()
    
        print("Record deleted...")


product_instance = StockCreateListRetrieveUpdateDelete(user="root",password="Password@123") 

# product_instance.post(product_name="powder",category="cosmetics",price=200,stock_quantity=5,supplier_name="tss")

# product_instance.get()

# product_instance.retrieve(id=1)

# product_instance.put(id=1,supplier_name="varun",price=450)

# product_instance.delete(id=5)

# product_instance.filter(category="cosmetics",price=250)     

# product_instance.summary()