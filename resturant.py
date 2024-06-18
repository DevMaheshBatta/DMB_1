from resturant_dish import Dish
from resturant_menu import Menu 

class Resturant:
    def __init__(self,name="NA",phone="NA",email="NA",address="NA",Operatinghours="10:00-23:00",menu="none"):
      self.name= name
      self.phone=phone
      self.email=email
      self.address=address
      self.operatinghours=Operatinghours
      self.menu=menu  
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Resturant: {}|{}|{}".format(self.name,self.phone,self.email,self.address,self.operatinghours))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
        self.menu.show()
dishes = [
        Dish(), 
        Dish("Dal Makhani", 250, 4.5),
        Dish(name="Paneer Masala", price=350, rating=4.5)
    ]
menu = Menu(
    name="Indian Veggie Delight", 
    number_of_dishes=len(dishes), 
    menu_dishes=dishes)

Resturant(name="Ludhiana Veggie Delight",
                        phone="+91 99999 11111",
                        email="veggies@abc.com",
                        address="Krishna Nagar", 
                        ratings=4.5,
                        menu=Menu(
                            name="Indian Veggie Delight", 
                            number_of_dishes=3, 
                            menu_dishes=[
                                        Dish(), 
                                        Dish("Dal Makhani", 250, 4.5),
                                        Dish(name="Paneer Masala", price=350, rating=4.5)
                                    ])
                        ).show()