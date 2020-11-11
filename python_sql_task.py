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

    # Create a method that adds a table to the database.
    # Choose your table name, column names and datatypes
    def create_table(self):
        # Request table name
        self.table_name = input("Enter table name: ")

        self.col_names = []
        # loop for as many columns the user wants
        while True:
            self.col_names.append([input("Enter column name: "), input("Enter column datatype and constraint (e.g VARCHAR(255): ")])
            if '' in self.col_names[-1]:
                self.col_names.pop(-1)
                break

        # Create table in database with first column
        self.cursor.execute(f"CREATE TABLE {self.table_name} ({self.col_names[0][0]} {self.col_names[0][1]});")
        # Add the rest of the table columns
        for col, data in self.col_names[1:]:
            self.cursor.execute(f"ALTER TABLE {self.table_name} ADD {col} {data};)")

    # create a method that lets user input data into the table
    def input_data(self):
        # Loop round the column names asking for an input
        values = []
        for col in self.col_names:
            values.append(input(f"please enter {col[0]} value: "))

        # Enter values into the table
        for _ in range(len(self.col_names)):
            # check the data types as to know whether to pass values in quotes or not
            if 'CHAR' in self.col_names[_][1]:
                self.cursor.execute(f"""
                INSERT INTO {self.table_name} ({self.col_names[_][0]})
                VALUES ('{values[_]}');
                """)
            else:
                self.cursor.execute(f"""
                INSERT INTO {self.table_name} ({self.col_names[_][0]})
                VALUES ({values[_]});
                """)

if __name__ == "__main__":
    northwind = Northwind()
    northwind.establish_connection()
    northwind.create_table()
    northwind.input_data()
    # Loop to add as much data as user wants
    while True:
        res = input("Do you want row?")
        if res[0].lower == 'n':
            break
        northwind.input_data()
