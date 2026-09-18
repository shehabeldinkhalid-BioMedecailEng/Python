# Database ---> PythonApplication_Database.py
from ast import Not
import sqlite3 
# cerate a connection to the database
connection = sqlite3.connect('shehab.db')
# create a tabel and insert data
# For cursor object
cursor = connection.cursor()
# create data into the table
cursor.execute("CREATE TABLE IF NOT EXISTS id_name (id_name INTEGER,user_name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER,user_id INTEGER)")
# insert data into the table
My_list=["Ahmed","Mohamed","shehab","Ream","Retage","nabel","belal","ziad","abderahman","hanan"]
for index,user_name in enumerate(My_list):
    cursor.execute(f"INSERT INTO id_name (id_name,user_name) VALUES ({index+1},'{user_name}')")


# update data in the table
cursor.execute("UPDATE id_name SET user_name = 'Mohamed' WHERE id_name = 2")

# delete data from the table --> cursor.execute("DELETE FROM id_name")

# To Select all data from the table ---> cursor.execute("SELECT * FROM id_name")
cursor.execute("SELECT user_name FROM id_name")
# fetch all data from the table
while True:
    item = cursor.fetchone() 
    if item is None:
        break
    # Only print the first item from the SELECT query
    print(item)

# save the changes in database external file
connection.commit()



# close the connection
cursor.close()
# DELETE CURSOR
connection.close()
# To delete the table ---> connection.execute("DROP TABLE IF EXISTS id_name")