# create python mysql book crud application that include insert,list,retrieve,update,delete of book

from mysql import connector

connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
)

cursor = connection.cursor()

query = """
        insert into book(title,total_pages,price,author) values(%s,%s,%s,%s)
"""

values = ("Chemmeen",250,450,"Thakazhi")

cursor.execute(query,values)

connection.commit()

print("Record added...")