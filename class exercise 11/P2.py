import sqlite3
import os

os.remove("/Users/tobisho/cmpr114/class exercise 11/P2.db")
con = sqlite3.connect("/Users/tobisho/cmpr114/class exercise 11/P2.db")
cur = con.cursor()

cur.execute('''CREATE TABLE Products
(ProductID INTEGER PRIMARY KEY NOT NULL,
Description TEXT,
UnitCost REAL,
RetailPrice REAL,
UnitsOnHand INTEGER)''')

cur.execute('''CREATE TABLE Warehouse
(WarehouseID INTEGER PRIMARY KEY NOT NULL,
ProductID INTEGER NOT NULL,
StorageLocation TEXT,
FOREIGN KEY (ProductID) REFERENCES Products(ProductID))''')

con.commit()

products_data = [
    (1, "Dark Chocolate Bar", 2.99, 5.99, 197),
    (2, "Medium Dark Chocolate Bar", 2.99, 5.99, 406),
    (3, "Milk Chocolate Bar", 2.99, 5.99, 266),
    (4, "Chocolate Truffles", 5.99, 11.99, 398),
    (5, "Chocolate Caramel Bar", 3.99, 6.99, 272),
    (6, "Chocolate Raspberry Bar", 3.99, 6.99, 363),
    (7, "Chocolate and Cashew Bar", 4.99, 9.99, 325),
    (8, "Hot Chocolate Mix", 5.99, 12.99, 222),
    (9, "Semisweet Chocolate Chips", 1.99, 3.99, 163),
    (10, "White Chocolate Chips", 1.99, 3.99, 293)
]

cur.executemany('''INSERT INTO Products
(ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
VALUES (?, ?, ?, ?, ?)''', products_data)

warehouse_data = [
    (100, 1, "South"),
    (200, 2, "South"),
    (300, 3, "East"),
    (400, 4, "West"),
    (500, 5, "West"),
    (600, 6, "MidWest"),
    (700, 7, "MidWest"),
    (800, 8, "East"),
    (900, 9, "East"),
    (1000, 10, "West")
]

cur.executemany('''INSERT INTO Warehouse
(WarehouseID, ProductID, StorageLocation)
VALUES (?, ?, ?)''', warehouse_data)

con.commit()

cur.execute('''SELECT * FROM Products''')
products_results = cur.fetchall()

print("Products Table:")
print(f'{"ProductID":<10} {"Description":<25} {"UnitCost":<10} {"RetailPrice":<12} {"UnitsOnHand":<12}')
print()
for row in products_results:
    print(f'{row[0]:<10} {row[1]:<25} {row[2]:<10} {row[3]:<12} {row[4]:<12}')

cur.execute('''SELECT * FROM Warehouse''')
warehouse_results = cur.fetchall()

print("\nWarehouse Table:")
print(f'{"WarehouseID":<12} {"ProductID":<10} {"StorageLocation":<15}')
print()
for row in warehouse_results:
    print(f'{row[0]:<12} {row[1]:<10} {row[2]:<15}')

con.close()