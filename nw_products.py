# Import pyodbc module to interact with SQL
import pyodbc

# create a class which establishes connection with northwind and can collect product table
class NWProducts:

    def __init__(self, username, password):
        server = "databases1.spartaglobal.academy"
        database = "Northwind"
        self.username = username
        self.password = password
        self.northwind_connection = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={self.username};PWD={self.password}')

        # create a class variable that's the cursor
        self.cursor = self.northwind_connection.cursor()

    def products(self):
        # make a query to collect all data from products table and story it in a variable
        query = "SELECT * FROM PRODUCTS;"
        products = self.cursor.execute(query).fetchall()
        # create a loop to show products table
        for row in products:
            print(row)