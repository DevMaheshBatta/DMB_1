#  coustmer=name, phone ,email,address ,gender,age

class Coustmer:
    def __init__(self,name="NA", phone="NA" ,email="NA",address="NA" ,gender="NA",age="NA"):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        self.gender=gender
        self.age=age

    def add_coustomer_detail (self):
       self.name=input("enter coustmer Name: ")
       self.phone=input("enter coustmer Phone: ")
       self.address=input("enter coustmer Address: ")
       self.gender=input("enter coustmer Gender: ")
       self.age= input("enter coustmer Age: ")

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Name {}| Phone {}| Email  {}| ".format ,self.name,self.phone,self.email)
        print("Address  {}|  Gender {}|  age {}" .format ,self.address,self.gender,self.age )
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

coustmer=Coustmer()
coustmer.add_coustomer_detail()
coustmer.show()


    