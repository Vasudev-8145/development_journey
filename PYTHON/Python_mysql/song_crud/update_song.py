
from mysql import connector

connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="song_db"
)

cursor = connection.cursor()

query = """
    update song set title=%s,movie=%s where id=%s
"""

values = ("engotta","balan",2)

cursor.execute(query,values)

connection.commit()

print("record updated")