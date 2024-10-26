import sqlite3
import os

os.remove("/Users/tobisho/cmpr114/class exercise 11/CE11.db")
con = sqlite3.connect("/Users/tobisho/cmpr114/class exercise 11/CE11.db")
cur = con.cursor()

cur.execute('''CREATE TABLE Products
(ProductID INTEGER PRIMARY KEY NOT NULL,
Description TEXT,
UnitCost REAL,
RetailPrice REAL,
UnitsOnHand INTEGER)''')

con.commit()

cur.execute('''INSERT INTO Products
(ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
VALUES
(1, "Dark Chocolate Bar", 2.99, 5.99, 197)''')

cur.execute('''INSERT INTO Products
(ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
VALUES
(2, "Medium Dark Chocolate Bar", 2.99, 5.99, 406)''')

cur.execute('''INSERT INTO Products
(ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
VALUES
(3, "Milk Chocolate Bar", 2.99, 5.99, 266)''')

cur.execute('''INSERT INTO Products
(ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
VALUES
(4, "Chocolate Truffles", 5.99, 11.99, 398)''')

cur.execute('''INSERT INTO Products
(ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
VALUES
(5, "Chocolate Caramel Bar", 3.99, 6.99, 272)''')

cur.execute('''INSERT INTO Products
(ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
VALUES
(6, "Chocolate Rasberry Bar", 3.99, 6.99, 363)''')

cur.execute('''INSERT INTO Products
(ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
VALUES
(7, "Chocolate and Cashew Bar", 4.99, 9.99, 325)''')

cur.execute('''INSERT INTO Products
(ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
VALUES
(8, "Hot Chocolate Mix", 5.99, 12.99, 222)''')

cur.execute('''INSERT INTO Products
(ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
VALUES
(9, "Semisweet Chocolate Chips", 1.99, 3.99, 163)''')

cur.execute('''INSERT INTO Products
(ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
VALUES
(10, "White Chocolate Chips", 1.99, 3.99, 293)''')

cur.execute('''Select * from Products''')

results = cur.fetchall()

print("ProductID, Description, UnitCost, RetailPrice, UnitsOnHand")
for row in results:
    print(f'{row[0]} {row[1]} {row[2]}, {row[3]}, {row[4]}')

con.close()