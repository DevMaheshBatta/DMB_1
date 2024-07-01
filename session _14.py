import mysql.connector as db
from session_13 import Customer


#data username and password
# username ="root"
#password=""
##local host
#host ="127.0.0.1"
#database="gw2024pds"


connection=db.connect (user="root",
                      password="devmahesh09",
                      host="127.0.0.1",
                      database="gw2024pds")
print("connection created")
print(connection)

customer=Customer()
customer.add_customer_details()

#create SQL Statement
sql = "insert into Customer values(null, '{}', '{}', '{}', {}, '{}')".format(customer.name, customer.phone, customer.email, customer.age, customer.gender)
cursor=connection.cursor()
cursor.execute(sql)
connection.commit()
print("SQL Statement Executed...")

