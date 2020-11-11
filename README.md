# Python with SQL
- **Using PYODBC (open database connectivity) to connect to SQL from our python program**

- **What is a cursor and how to use it**

- **Some functions that we can use to interact with SQL data**

![](/python_with_sql.png)

- set up PYODBC connection
- command to install PYODBC
```pip install pyodbc```
- Before you do anything, makes sure you have downloaded a pyodbc driver. You can download it from the following link:
```
https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
```

**Establish connection**
```python
import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "****"
password = "******"
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
```
- server name - database name - username and password is required to connect to to pyodbc
- Verify our connection
```python
cursor = northwind_connection.cursor()
# cursor is location of your mouse / current path
cursor.execute("SELECT @@VERSION")
# Select version of current DB
row = cursor.fetchone() #shows the version of database
print(row)
```
- Run a query that fetches all the rows in the table Customers
```python
# In our DB we have a table called Customers that has customers data available
cust_row = cursor.execute("SELECT * FROM Customers;").fetchall()
# using fetchall() method we can get all the data available inside Customers table
print(cust_row)
# loop round each row and print the tuple
for records in cust_row:
    print(records)
```
- Query that gets just the unit price of products
```python
product_rows = cursor.execute("SELECT * FROM Products").fetchall()
# running queries in our python program to access database and table inside the DBs
for product_records in product_rows:
# iterate through the table data and find the unit prices
   print(product_records.UnitPrice)
```
- Another Query of collecting and printing UnitPrice Data
```python
product_row = cursor.execute("SELECT * FROM Products")
# getting the product table data
# Iterating through the data until the last line of the data (until condition is False)
# combination of our loop and control flow to ensure we only iterate through the data as long as the data is available
while True:
    records = product_row.fetchone()
    if records is None:
        # when there are no records left (value is None) stop
        break
    print(records.UnitPrice)
```
