# import the pyodbc module to interact with SQL
import pyodbc

#import nw_products class
from nw_products import NWProducts

# create a nw runner class that is a child of the nw products class and can print the average value of the stocks
class NWRunner(NWProducts):
    def __init__(self, username, password):
        # import the password and username attributes
        super().__init__(username, password)

    # define a function that finds the average value of UnitStock price
    def average_stock(self):
        stocks = self.cursor.execute("SELECT UnitsInStock FROM Products;").fetchall()
        # convert the stocks dictionary to integer values
        stocks_in_integer = []
        for stock in stocks:
            stocks_in_integer.append(int(stock[0]))
        # returns the average from the integer stocks list
        return sum(stocks_in_integer)/len(stocks_in_integer)

if __name__ = "__main__":
    obj = NWRunner("**", "****")
    print(obj.average_stock())
