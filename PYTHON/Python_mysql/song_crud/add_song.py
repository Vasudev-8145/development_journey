# establish connection

from mysql import connector

connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="song_db"
)

cursor = connection.cursor()

query = """
    insert into song(title,track_number,movie,singers) values(%s,%s,%s,%s)
"""

values = ("karimizhi",5,"killadi","chacha")

cursor.execute(query,values)

connection.commit()
connection.close()

print("Record has been added...")