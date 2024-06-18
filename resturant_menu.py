from resturant_dish import Dish 
class Menu:
    def __init__(self,name="NA",number_of_dishes=0,menu_dishes=[]):
        self.name=name
        self.number_of_dishes=number_of_dishes
        self.menu_dishes=menu_dishes

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Menu: {}|{}|{}".format(self.name,self.number_of_dishes,self.menu_dishes))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

       # print("Dishes")
        #for idx in range (len (self.menu_dishes)):
        
         #self.menu_dishes[idx].show()


dishes=[Dish(),
        Dish("dal Makhni"),
        Dish("paneer masala ",price=340)]
menu=Menu(
   name="indian Veggies Delight"
   ,number_of_dishes=len(dishes),
   menu_dishes= dishes
)
menu.show()
