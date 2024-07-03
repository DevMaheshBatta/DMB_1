"""
create table Patient(
pid int primary key auto_increment,
name varchar(256),
phone varchar(150),
email varchar(256),
age int,
gender varchar(256),
created_on datetime );
"""
import datetime 

class Patient:

    def __init__(self, pid=0,name="",phone="",email="",age=0,gender=""):
        self.pid=pid
        self.name=name
        self.phone=phone
        self.email=email
        self.age=age
        self.gender=gender
        self.created_on=datetime.datetime.now()
      


    def add_patient_details(self):
        print(">> ENTER PATIENT DETAILS")
        self.name = input("Enter PATIENT  Name: ")
        self.phone = input("Enter PATIENT Phone: ")
        self.email = input("Enter PATIENT Email: ")
        self.age = int(input("Enter PATIENT Age: "))
        self.gender = input("Enter PATIENT Gender: ")
        #we will not get input from created on
        #created on is system data time stamp

      # def update_customer_details(self):
    #     choice = input("Do you wish to update Name (yes/no)")
    #     if choice == "yes":
    #         self.name = input("Enter Customer Name: ")
    def update_patient_details(self):
        name = input("Enter Patient Name: ")
        if len(name) != 0:
            self.name = name

    #     self.phone = input("Enter Customer Phone: ")
    #     self.email = input("Enter Customer Email: ")
    #     self.age = int(input("Enter Customer Age: "))
    #     self.gender = input("Enter Customer Gender: ")
        phone = input("Enter Patient Phone: ")
        if len(phone) != 0:
            self.phone = phone

        email = input("Enter Patient Email: ")
        if len(email) != 0:
            self.email = email

        age = input("Enter Patient Age: ")
        if len(age) != 0:
            self.age = int(age)

        gender = input("Enter Patient  Gender: ")
        if len(gender) != 0:
            self.gender = gender
    


    def show(self):
        print("~~~~~~~PATIENT~~~~~~~~~~~") 
        print("{} | {} | {} ".format(self.name,self.phone,self.email)) 
        print("{} | {}  ".format(self.age,self.gender))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~") 

        
         