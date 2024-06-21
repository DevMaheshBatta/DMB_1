#  Customer: name, phone, email, address, gender, age
class Customer:

    def __init__(self, name="", phone="", 
                 email="", address="", gender="", age=15):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.gender = gender
        self.age = age

    def add_customer_details(self):
        print(">> ENTER CUSTOMER DETAILS")
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")
        self.address = input("Enter Customer Address: ")
        self.gender = input("Enter Customer Gender: ")
        self.age = int(input("Enter Customer Age: "))


    def show(self):
        print("------------------CUSTOMER-----------------")
        print("Name: {} | Phone: {}".format(self.name, self.phone))
        print("Email: {} | Address: {}".format(self.email, self.address))
        print("Gender: {} | Age: {}".format(self.gender, self.age))
        print("------------------------------------------")

    def to_csv(self):
        # John,+91 98765 12345,john@example.com,Redwood Shores,male,32
        data = "{},{},{},{},{},{}\n".format(self.name, 
                                            self.phone, self.email, self.address, self.gender, self.age)
        return data
"""38 changes: 38 additions & 0 deletions38  
Session11A.py
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,38 @@"""
from Session11 import Customer

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to Customer Management System")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:

    print("1: Add Customer")
    print("2: View Customers")
    print("0: Quit")

    choice = int(input("Enter Your Choice: "))
    print("You Selected:", choice)

    if choice == 1:
        file = open("customers.csv", "a")
        customer = Customer()
        customer.add_customer_details()
        customer.show()

        data = customer.to_csv()
        file.write(data)
        print("Data Written:", data)

    elif choice == 2:
        file = open("customers.csv", "r")
        lines = file.readlines()
        for line in lines:
            print(line)

    elif choice == 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Thank You for using Customer Management")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        file.close()
        break

#  14 changes: 14 additions & 0 deletions14  
# Session11B.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,14 @@
quote1 = "Search the candle rather than cursing the darkness\n"
quote2 = "Be Exceptional\n"

# file = open("quotes.txt", "w")
file = open("quotes.txt", "a")
file.write(quote1)
file.write(quote2)

# Free memory resource once, you have used file
file.close()

print("Data Written...")


#  11 changes: 11 additions & 0 deletions11  
# Session11C.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,11 @@
name = input("Enter Customer Name: ")
phone = input("Enter Customer Phone: ")
email = input("Enter Customer Email: ")

customer_details = "{},{},{}\n".format(name, phone, email)

# file = open("/Users/ishant/Downloads/customers.csv", "a")
file = open("customers.csv", "a")
file.write(customer_details)
print("Customer Data Saved..")
file.close()
# 10 changes: 10 additions & 0 deletions10  
# Session11D.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,10 @@
file = open("customers.csv", "r")
# data = file.read()

lines = file.readlines()

print("File Data:")
print(lines)

for i in range(len(lines)):
    print(lines[i])
#  57 changes: 57 additions & 0 deletions57  
# Session11E.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,57 @@
"""
    Driver has a vehicle
    Customer can book Ride(s)
    Identiy Objects with attributes
    Vehicle: reg_number, brand, model, color
    Driver:  name, phone, email, license_number, rating, gender, age, vehicle [1 to 1]
    1 Driver has 1 Vehicle
    Customer: name, phone, email, address, gender, age
    Ride: customer [1 to 1], date, time, from_location, to_location, distance, fare, driver [1 to 1]
    1 Ride has 1 Customer
    1 Ride has 1 Driver
"""

class Ride:

    def __init__(self, customer=None, date="20th June, 2024", time="12:00", 
                 from_location="Home", to_location="Work", otp=3027,
                 distance=4, fare=200, driver=None):
        self.customer = customer
        self.date = date
        self.time = time
        self.from_location = from_location
        self.to_location = to_location
        self.otp = otp
        self.distance = distance
        self.fare = fare
        self.driver = driver


    def add_ride_details(self):
        print(">> ENTER RIDE DETAILS")
        self.from_location = input("Enter From Location: ")
        self.to_location = input("Enter To Location: ")

    def link_customer(self, customer):
        self.customer = customer

    def link_driver(self, driver):
        self.driver = driver

    def show(self):

        self.customer.show()

        print("------------------RIDE-----------------")    
        print("FROM: {} | TO: {}".format(self.from_location, self.to_location))
        print("DISTANCE: {} | FARE: {}".format(self.distance, self.fare))
        print("DATE: {} | TIME: {}".format(self.date, self.time))
        print("OTP: {} ".format(self.otp))
        print("------------------------------------------")

        self.driver.show()
#  21 changes: 21 additions & 0 deletions21  
# Session11F.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,21 @@
# from Session10C import Vehicle
# from Session10D import Driver
# from Session11 import Customer
# from Session11E import Ride

# Driver Application
driver = Driver()
driver.add_driver_details()

# Customer Application
customer = Customer()
customer.add_customer_details()

# Server
ride = Ride()
ride.add_ride_details()
ride.link_customer(customer)
ride.link_driver(driver)

print("RIDE BOOKED....")
ride.show()