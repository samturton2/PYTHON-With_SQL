# Python SQL Task walkthrough
### Task
- Create a new file and a class with function to establish connection with pyodbc
- create a function that create a table in the DB
- create a function that prompts user to input data in that table
- create a new file called PYODBC_TASK.md and document the steps to implement the task

### Walkthrough
- Create a new file and import the pyodbc module
```python
import pyodbc
```
- Create a class that holds methods for the northwind database
```python
class Northwind:
```
- Create a method that connects to the database
```python   
    def establish_connection(self):
        server = "databases1.spartaglobal.academy"
        database = "Northwind"
        username = "SA"
        password = "********"
        self.northwind_connection = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')
        #create a class variable that's the cursor
        self.cursor = self.northwind_connection.cursor()
```
- Create a method that adds a table to the database.
- You should be able to choose your table name, column names and datatypes
- make sure to store the table name and the columns names as class wide variables so we can use them later using `self.`
```python    
    def create_table(self):
        # Request table name
        self.table_name = input("Enter table name: ")

        self.col_names = []
        # loop for as many columns the user wants
        while True:
        # store each collumn name and datatype pair as an inbedded list in the col_names list
            self.col_names.append([input("Enter column name: "), input("Enter column datatype and constraint (e.g VARCHAR(255): ")])
            if '' in self.col_names[-1]:
                self.col_names.pop(-1)
                break
```
- In the same method use self.cursor.execute() to write an SQL query and create table in database with first column
```python
        self.cursor.execute(f"CREATE TABLE {self.table_name} ({self.col_names[0][0]} {self.col_names[0][1]});")
```
- Add the rest of the table columns using SQL command `ALTER TABLE` and a for loop
```python
        for col, data in self.col_names[1:]:
            self.cursor.execute(f"ALTER TABLE {self.table_name} ADD {col} {data};)")
```
- create a method that lets user input data into the the new table
```python   
    def input_data(self):
```
- Loop round the column titles asking for an input
- make sure to specify the data type the user should enter
```python
        values = []
        for col, data in self.col_names:
            values.append(input(f"please enter {col} value in {data} form: "))
```
- Enter values into the table using the sql `INSERT INTO` command
```python        
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
```
- create test using all the functions to create a table if ran from class file
```python
if __name__ == "__main__":
    northwind = Northwind()
    northwind.establish_connection()
    northwind.create_table()
    northwind.input_data()
```
- Add a while loop to add as much data to the new table as the user wants
```python
    while True:
        res = input("Do you want row?")
        if res[0].lower == 'n':
            break
        northwind.input_data()
```