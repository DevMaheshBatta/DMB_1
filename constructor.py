# class loginpage:

#     def __init__(self): #self is refern=ence variable
#         print("self:",self)
#         self.name="shivam"
#         self.email="shivam123@gmail.com"
#         self.otp="2456"
#         self.phone="8360924444"
        

# login1=loginpage()
# print("login1 ", login1)    
# print("login 1 data")
# print(vars(login1))

# login2=loginpage()
# print("login2 ", login1)    
# print("login 2 data")
# print(vars(login2))

#hw resturant
#menu
#dishes
#resturant
# class resturants:
#     def __init__(self):
#         print( "self",self)
#         self.type="chinese"
#         self.categeory="veg resturant"
#         self.location="civil lines"
#         self.rating="4.5"
#         self.dishes="prantha, sabji,roti"

# resturant1=resturants ()
# print("resturant 1 ", resturant1)    
# print("Resturant 1 data")
# print(vars(resturant1))

# resturant2=resturants()
# print("resturant 2 ", resturant2)    
# print("Resturant 2 data")
# print(vars(resturant2))

#-------------------dishes
class Menu:
    def __init__(self):
        print( "self",self)
        self.type="chiness,south indian"
        self.categeory="veg "
        self.time="break fast,lunch ,dinner"
    
        self.dishes="prantha, sabji,roti"

menu1=Menu ()
print("menu 1 ", menu1)    
print("Menu data")
print(vars(menu1))

menu2=Menu()
print("menu 2 ", menu2)    
print("menu2 data")
print(vars(menu2))