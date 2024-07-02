
"""
create table Consultaion(
cid int primary key auto_increment,
pid int,
remarks varchar(256),
medicines varchar(256),
next_followup datetime,
created_on datetime,
FOREIGN KEY (pid) REFERENCES Patient (pid)
);

"""

import datetime

class Consultation:

    def __init__(self, cid=0,pid=0,remarks="",medicines="",next_followup=""):
        self.cid=cid
        self.pid=pid
        self.remarks=remarks
        self.medicines=medicines
        self.next_followup=next_followup
        self.created_on=datetime.datetime.now()

    def add_consultation_details(self):
        self.pid = input("Enter Patient ID: ")
        self.remarks = input("Enter Consultation Remarks: ")
        self.medicines = input("Enter Medicines: ")
        self.next_followup = input("Enter next_followup (yyyy-mm-dd hh:mm:ss): ")  





    def update_consultation_details(self):
        remarks = input("Enter new remarks: ")
        if len(remarks) != 0:
            self.remarks = remarks

    #     self.phone = input("Enter Customer Phone: ")
    #     self.email = input("Enter Customer Email: ")
    #     self.age = int(input("Enter Customer Age: "))
    #     self.gender = input("Enter Customer Gender: ")
        medicines = input("Enter new medicines: ")
        if len(medicines) != 0:
            self.medicines= medicines

        next_follwup = input("Enter new  followup: ")
        if len(next_follwup) != 0:
            self.next_followup = next_follwup

        
 


    def show(self):
        print("~~~~~~~Consultaion~~~~~~~~~~~") 
        consultation= """
        {cid}|{pid}|{remarks}
        {medicines}| {next_followup}|{created_on}""".format_map(vars(self))
        print(consultation)

        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
