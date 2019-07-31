import pyodbc

#Variables to connect to DB
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'


docker_northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

#What is a cursor?
cursor = docker_northwind.cursor()
#This is us executing a SQL query
cursor.execute("SELECT * FROM Customers;")

#From the cursor we can fetch one row
# row = cursor.fetchone()
# print(row)

#We can also Fetch all rows
all_customers = cursor.execute("SELECT * FROM Customers;").fetchall()  #...Fetch all is Dangerous as it can block our CPU with huge amount of data!

# print (all_customers)

# for row in all_customers:
#     print(row.ContactName, row.Fax)

#Because this is dangerous, we can use a while loop to fetchone() until record/row is none(break)

all_products = cursor.execute("SELECT * FROM Products;")

#This is more efficient than fetchall()
while True:
    row_record = all_products.fetchone()
    if row_record is None:
        break
    print(row_record.UnitPrice)

#We can use column name to retrieve specific data

all_null_fax = cursor.execute("SELECT ContactName, CompanyName, Phone FROM Customers WHERE Fax IS NULL;")
while True:
    row_record = all_null_fax.fetchone()
    if row_record is None:
        break
    print(row_record.ContactName,'--', row_record.CompanyName,'-- Phone:', row_record.Phone)

