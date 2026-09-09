# pip install mysql-connector-python

#step1 - import connector frpm mysql module

from mysql import connector

#step2 - import connector from mysql module

connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost"
)

print(connection)