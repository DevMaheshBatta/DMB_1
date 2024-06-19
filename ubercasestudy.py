"""
Driver has a vehicle
coustmer can book a ride



vehicle =reg_number,brand,model,color
Driver=name,phone,email,licence,rating,age,gender,vehicle,
coustmer=name, phone ,email,address ,gender,age
Ride=coustmer,date,time,,From location ,To locationfare,driver[1 to 1]
1 ride has 1 customer
1 ride has 1 driver


"""


class Vehicle:
    def  __init__(self,reg_number="NA",brand="NA",model="NA",color="white"):
     self.reg_number=reg_number
     self.brand=brand
     self.model=model
     self.color=color


    def add_vehicle_details(self):
      self.reg_number=input("enter vehicle reg number ")
      self.brand=input("enterbrand name")
      self.model=input("enter model")
      self.color=("enter color ")


    def show(self):
      print("--------------VEHICLE-------------------------")
      print("Number: {} | Brand: {}".format(self.reg_number, self.brand))
      print("Model: {} | Color: {}".format(self.model, self.color))
      print("-----------------------------------------------")
      
vehicle = Vehicle()
vehicle.add_vehicle_details()
vehicle.show()
      