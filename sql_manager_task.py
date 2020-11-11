# import the pyodbc module
import pyodbc

# establish connection with the northwind db
server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
northwind_connection = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')
#create a variable that's the cursor
cursor = northwind_connection.cursor()

