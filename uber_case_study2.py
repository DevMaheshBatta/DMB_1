from  ubercasestudy import Vehicle 

class Driver:
    def  __init__ (self,name="NA",phone="NA",email="NA",licence="NA",rating="NA",age="NA",gender="NA",vehicle="NA"):
     self.name=name
     self.phone=phone
     self.email=email
     self.licence=licence
     self.rating=rating
     self.age=age
     self.gender=gender
     self.vehicle=vehicle

    def add_driver_details(self):
      self.name=input("enter driver name")
      self.phone=input("enter  driver phone ")
      self.email=input("enter driver email")
      self.licence=input("enter driver licence Number")
      self.rating=input("enter driver rating")
      self.age=input("enter driver age")
      self.gender=input("enter driver gender")
      self.vehicle=input("enter driver vehicle")
      self.vehicle=Vehicle()
      self.vehicle.add_vehicle_details

    def show(self):
        print("-------------DRIVER--------------------------")
        print("Name: {} | Phone: {} | Email: {} ".format(self.name, self.phone,self.email))
        print("Licence: {} | Rating: {}| Age:  {}".format(self.licence, self.rating,self.age))
        print("gender: {}| Vehicle {}".format(self.gender,self.vehicle))

        self.vehicle.show()



driver=Driver()
driver.add_driver_details()
driver.show()