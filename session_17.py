"""
doctor->user of application
paitent :pid ,name,phone,email,dob,gender,created_on
consultaion : cid ,pid,remarks,medicines,next folloup,created_on,

"""
import datetime

"""
create table Patient(
pid int primary key auto_increment,
name varchar(256),
phone varchar(150),
email varchar(256),
dob date,
gender varchar(256),
created_on datetime );

"""

class Patient:

    def __init__(self, pid=0, name="", phone="", email="", dob="", gender=""):
        self.pid = pid
        self.name = name
        self.phone = phone
        self.email = email
        self.dob = dob
        self.gender = gender
        self.created_on = datetime.datetime.now()

    def add_patient_details(self):
        self.name = input("Enter Patient Name: ")
        self.phone = input("Enter Patient Phone: ")
        self.email = input("Enter Patient Email: ")
        self.dob = input("Enter Patient DOB (yyyy-mm-dd): ")
        self.gender = input("Enter Patient Gender: ")


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
        print("======Patient=======")

        patient = """
        {pid} | {name}  | {phone}
        {email} | {dob}
        {gender}| {created_on} 
        """.format_map(vars(self))

        print(patient)

        print("====================")
