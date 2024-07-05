from session_17 import Patient
from session_17A import Consultation
from session_15A import Database
from tabulate import tabulate 


def main():
    print("WELCOME TO DOCTOR'S APP")
    print("------------------")
    db=Database()
    while True:
        print("1: Add New Patient")
        print("2: Update Existing Patient")
        print("3: Delete Existing Patient")
        print("4: View Patient By Phone")
        print("5: View Patient By CID")
        print("6: View All Patient")
        print("7: Add New  Consulation")
        print("8: View All Consultation")
        print("9: View Consultation of Patient")
        print("10: View FollowUps")
        print("11:update consultation")
        print("0: To Quit App")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            patient = Patient()
            patient.add_patient_details()
            sql = "insert into Patient values(null, '{name}', '{phone}', '{email}', '{dob}','{gender}', '{created_on}')".format_map(vars(patient))
            db.write(sql)
            print("[ DOCTOR'S App]", patient.name, "Saved in DataBase")

        elif choice == 2:
            pid = int(input("Enter Patient ID to Update: "))
            sql = "select * from Patient where cid = {}".format(pid)
            rows = db.read(sql)
            print(rows)

            patient = Patient(pid=rows[0][0], name=rows[0][1], phone=rows[0][2], email=rows[0][3],dob=rows[0][4], gender=rows[0][5],created_on=rows[0][6])

            columns = ["pid", "name", "phone", "email", "gender", "dob","created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            print("Patient to Update:")
            patient.show()
            patient.update_patient_details()

            sql = "update  Patient set name = '{name}', phone='{phone}', email='{email}',dob='{dob}', gender='{gender}', created_on='{created_on}' where pid = {pid}".format_map(vars(patient))

            db.write(sql)

            patient.show()

        elif choice == 3:
            pid = int(input("Enter Patient ID to be Deleted: "))
            sql = "delete from Patient where pid = {}".format(pid)
            ask = input("Are you sure to delete? (yes/no): ")
            if ask == "yes":
                db.write(sql)
                print("[DOCTOr'S APP]", pid, "Deleted from DataBase")
            else:
                print("Delete Operation Skipped")   
        
        elif choice == 4:
            phone = input("Enter Patient Phone Number: ")
            sql = "select * from Patient where phone = '{}'".format(phone)
            rows = db.read(sql)
            columns = ["pid", "name", "phone", "email","dob", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
        elif choice == 5:
            pid = int(input("Enter Patient ID: "))
            sql = "select * from Patient where pid = {}".format(pid)
            rows = db.read(sql)
            columns = ["pid", "name", "phone", "email","dob", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
        elif choice == 6:
            sql = "select * from Patient"
            rows = db.read(sql)
            columns = ["pid", "name", "phone", "email","dob","gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))


        elif choice == 7:
            consultation =Consultation()
            consultation.add_consultation_details()
            sql = "insert into Consultation values(null, {pid}, '{remarks}', '{medicines}', '{next_followup}', '{created_on}')".format_map(vars(consultation))
            db.write(sql)
            print("Consultation Created..")
        elif choice == 8:
        
         sql= "select * from Consultation" 
         rows = db.read(sql)

         columns = ["cid", "pid", "remarks", "medicines", "next_followup", "created_on"]  
         print(tabulate(rows, headers=columns, tablefmt='grid'))

        elif choice == 9:
            pid = int(input("Enter Patient ID: "))
            sql = "select * from Consultation where pid = {}".format(pid)
            rows = db.read(sql)
            columns = ["cid", "pid", "remarks", "medicines", "next_followup", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid')) 

        elif choice == 10:
            start_date = input("Enter Start Date Time(yyyy-mm-dd hh:mm:ss): ")
            end_date = input("Enter End Date Time(yyyy-mm-dd hh:mm:ss): ")

            sql = "select * from Consultation where next_followup >= '{}' and next_followup <= '{}'".format(start_date, end_date)
            rows = db.read(sql)

            columns = ["cid", "pid", "remarks", "medicines", "next_followup", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))     

        elif choice == 11:
            cid = int(input("Enter consultation ID to Update: "))
            sql = "select * from consultation where cid = {}".format(cid)
            rows = db.read(sql)
            print(rows)
            consultation = Consultation(pid=rows[0][0],cid=rows[0][1], remarks=rows[0][2], medicines=rows[0][3], next_followup=rows[0][4])

            columns = ["pid","cid", "remarks", "medicines", "next_followup","created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            print("Consultation to Update:")
            consultation.show()
            consultation.update_consultation_details()

            sql = "update  Patient set remarks = '{remarks}', medicines='{medicines}', next_follwup='{next_followup}', created_on='{created_on}' where cid = {cid}".format_map(vars(consultation))

            db.write(sql)

            consultation.show()


        elif choice == 0:
          break
        else:
            print("DOCTOR'S APP Invalid Choice", choice)

if __name__ == "__main__":
    main()



