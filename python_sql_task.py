# import the pyodbc module
import pyodbc

# Create a class that holds methods for the northwind database
class Northwind:

    # Create a method that connects to the database
    def establish_connection(self):
        server = "databases1.spartaglobal.academy"
        database = "Northwind"
        username = "SA"
        password = "Passw0rd2018"
        self.northwind_connection = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')
        #create a class variable that's the cursor
        self.cursor = self.northwind_connection.cursor()

    # Create a method that adds a table to the database
    def create_4_column_varchar_table(self):
        self.column1 = input("column1 title: ")
        self.column2 = input("column2 title: ")
        self.column3 = input("column3 title: ")
        self.column4 = input("column4 title: ")
        self.cursor.execute(f"""
        CREATE TABLE new_table ( 
            {self.column1} varchar(255),
            {self.column2} varchar(255),
            {self.column3} varchar(255),
            {self.column4} varchar(255)
            );
        """)

    # create a method that lets user input data into the table
    def input_data(self):
        value1 = input(f"{self.column1} row value: ")
        value2 = input(f"{self.column2} row value: ")
        value3 = input(f"{self.column3} row value: ")
        value4 = input(f"{self.column4} row value: ")
        cursor.execute(f"""
        INSERT INTO new_table ({self.column1}, {self.column2}, {self.column3}, {self.column4})
        VALUES ({value1}, {value2}, {value3}, {value4});
        """)


northwind = Northwind()
northwind.establish_connection()
northwind.create_4_column_varchar_table('name', 'colour', 'hat', 'gloves')