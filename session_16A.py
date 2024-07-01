
from session_16 import Patient
from session_15A import Database
from tabulate import tabulate       # pip install tabulate
def main():
    print("-------------------")
    print("WELCOME to PMS APP")
    print("-------------------")
    db = Database()
    while True:
        print("1: Add New Patient")
        print("2: Update Existing Patient")
        print("3: Delete Existing Patient")
        print("4: View Patient By Phone")
        print("5: View Patient By CID")
        print("6: View All Patient")
        print("0: To Quit App")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            patient = Patient()
            patient.add_patient_details()
            sql = "insert into Patient values(null, '{name}', '{phone}', '{email}', {age}, '{gender}', '{created_on}')".format_map(vars(patient))
           # sql = "insert into Customer values(null, '{}', '{}', '{}', {}, '{}', null)".format(customer.name, customer.phone, customer.email, customer.age, customer.gender)
            db.write(sql)
            print("[PMS App]", patient.name, "Saved in DataBase")
        elif choice == 2:
            cid = int(input("Enter Patient ID to Update: "))
            sql = "select * from Patient where cid = {}".format(cid)
            rows = db.read(sql)
            print(rows)

            patient = Patient(cid=rows[0][0], name=rows[0][1], phone=rows[0][2], email=rows[0][3], age=rows[0][4], gender=rows[0][5])

            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            print("Patient to Update:")
            patient.show()
            patient.update_patient_details()

            sql = "update  Patient set name = '{name}', phone='{phone}', email='{email}', age={age}, gender='{gender}', created_on='{created_on}' where cid = {cid}".format_map(vars(patient))

            db.write(sql)

            patient.show()


        elif choice == 3:
            cid = int(input("Enter Patient ID to be Deleted: "))
            sql = "delete from Customer where cid = {}".format(cid)
            ask = input("Are you sure to delete? (yes/no): ")
            if ask == "yes":
                db.write(sql)
                print("[CMS App]", cid, "Deleted from DataBase")
            else:
                print("Delete Operation Skipped")
        elif choice == 4:
            phone = input("Enter Patient Phone Number: ")
            sql = "select * from Patient where phone = '{}'".format(phone)
            rows = db.read(sql)
            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
        elif choice == 5:
            cid = int(input("Enter Patient ID: "))
            sql = "select * from Patient where cid = {}".format(cid)
            rows = db.read(sql)
            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
        elif choice == 6:
            sql = "select * from Patient"
            rows = db.read(sql)
            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            
            # for row in rows:
            #     print(row)
        elif choice == 0:
            break
        else:
            print("[CMS APP] Invalid Choice", choice)

if __name__ == "__main__":
    main()