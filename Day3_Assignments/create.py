
# import module of mysql connector
import mysql.connector

# create a connection with mysql database server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

# create a query
Empid = int(input("Enter Empid : "))
Name = input("Enter Name : ")
Department = input("Enter Department :")
email = input("Enter email :")
Salary = float(input("Enter Salary : "))
DoJ = input("Enter DoJ : ")


query = f"insert into Employee values({Empid}, '{Name}', '{Department}', '{email}', {Salary}, '{DoJ}');"

# create a cursor to execute the query
cursor = connection.cursor()

# execute query using cursor
cursor.execute(query)

# after execution of query commit your changes
connection.commit()

# close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()