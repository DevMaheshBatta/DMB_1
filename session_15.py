
"""
create table Customer(
cid int primary key auto_increment,
name varchar(256),
phone varchar(150),
email varchar(256),
age int,
gender varchar(256),
created_on datetime );
"""

import datetime 

class Customer:

    def __init__(self, cid=0,name="",phone="",email="",age=0,gender=""):
        self.cid=cid
        self.name=name
        self.phone=phone
        self.email=email
        self.age=age
        self.gender=gender
        self.created_on=datetime.datetime.now()
      


    def add_customer_details(self):
        print(">> ENTER CUSTOMER DETAILS")
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")
        self.age = int(input("Enter Customer Age: "))
        self.gender = input("Enter Customer Gender: ")
        #we will not get input from created on
        #created on is system data time stamp


    def show(self):
        print("~~~~~~~CUSTOMER~~~~~~~~~~~") 
        print("{} | {} | {} ".fromat(self.name,self.phone,self.email)) 
        print("{} | {} | {} ".fromat(self.age,self.gender))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~") 

        
         