# class loginpage:

#     def __init__(self): #self is refernence variable
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

#---------------------
class Dish:

    # Parameterized Constructor, with default values of arguments passed to it
    def __init__(self, name="NA", price=0, rating=1.5):
        # print(">> self is: {}".format(self))
        # copy the contents of name (input to constructor) into self.name (attribute of object)
        self.name = name 
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Dish: {} | {} | {}".format(self.name, self.price, self.rating))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


# dish1 = Dish()
# print("dish1:", hex(id(dish1)))

# dish2 = Dish("Dal Makhani", 250, 4.5)
# print("dish2:", hex(id(dish2)))

# dish3 = Dish(name="Paneer Masala", price=350, rating=4.5)
# print("dish2:", hex(id(dish3)))



# List of Dishes

dishes = [
        Dish(), 
        Dish("Dal Makhani", 250, 4.5),
        Dish(name="Paneer Masala", price=350, rating=4.5)
    ]
print("DISHES:\n")
for idx in range(len(dishes)):
    dishes[idx].show()

