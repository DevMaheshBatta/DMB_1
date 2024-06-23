"""
i:0             10, 30, 50, 20, 40
j:0-3 j: 0      10, 30, 50, 20, 40
j:0-3 j: 1      10, 30, 50, 20, 40
j:0-3 j: 2      10, 30, 20, 50, 40
j:0-3 j: 3      10, 30, 20, 40, 50
i:1             10, 30, 20, 40, 50
j:0-2 j:0       10, 30, 20, 40, 50
j:0-2 j:1       10, 20, 30, 40, 50
j:0-2 j:2       10, 20, 30, 40, 50
i:2             10, 30, 20, 40, 50
j:0-1 j:0       10, 30, 20, 40, 50
j:0-1 j:1       10, 20, 30, 40, 50
i:3             10, 30, 20, 40, 50
j:0   j:0       10, 30, 20, 40, 50
"""

def bubble_sort(data):
    for i in range(len(data)-1):
        print("i is:", i)
        for j in range(len(data)-i-1):
            print(j, end=" ")

            if data[j] > data[j+1]:
                print("Swapping {} with {}".format(data[j], data[j+1]))
                # Swap Operation
                data[j], data[j+1] = data[j+1], data[j]

        print()

numbers = [10, 30, 50, 20, 40]

print("UnSorted Numbers:")
print(numbers)
print("~~~~~~~~~~~~~~~~~~~~~")
bubble_sort(numbers)
print("Sorted Numbers:")
print(numbers)

# HW: Explore different sorting techniques
 
# Dish: name, price, rating

class Dish:

    def __init__(self, name="", price=0, rating=1.5):
          self.name = name
          self.price = price
          self.rating = rating

    def show(self):
        print("--------Dish--------")
        print("{} | {} | {}".format(self.name, self.price, self.rating))
        print("--------------------")


# Outside the class
def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j].price > data[j+1].price:
            # if data[j].rating < data[j+1].rating:
                # Swap Operation
                data[j], data[j+1] = data[j+1], data[j]

# HW: Implement different sorting techniques on List of Dishes
# List of Dish Objects

"""
dish1 = Dish(name="Dal Makhani", price=250, rating=4.5)
dish2 = Dish(name="Paneer Makhani", price=400, rating=4.2)
dish3 = Dish(name="Noodles", price=300, rating=3.5)
dish4 = Dish(name="Pizza", price=650, rating=4.0)
dish5 = Dish(name="Burger", price=50, rating=3.1)
# dishes = [dish1, dish2, dish3, dish4, dish5]
"""

dishes = [
          Dish(name="Dal Makhani", price=250, rating=4.5), 
          Dish(name="Paneer Makhani", price=400, rating=4.2), 
          Dish(name="Noodles", price=300, rating=3.5), 
          Dish(name="Pizza", price=650, rating=4.0), 
          Dish(name="Burger", price=50, rating=3.1)
          ]

# for idx in range(len(dishes)):
#      dishes[idx].show()
print("DISHES:")
for dish in dishes:
     dish.show()

bubble_sort(dishes)


print("SORTED DISHES:")
for dish in dishes:
     dish.show()

"""
    OOPS case Study for the Day. Food Delivery App.
    
    Customer
    Dish
    Order
    1 Customer can place many Orders
    1 Order can have many Dishes
"""

class Dish:

    def __init__(self, name="", price=0, rating=1.5):
          self.name = name
          self.price = price
          self.rating = rating

    def show(self):
        print("--------Dish--------")
        print("{} | {} | {}".format(self.name, self.price, self.rating))
        print("--------------------")



class Customer:

    def __init__(self, name="", phone="", email="", address=""):
          self.name = name
          self.phone = phone
          self.email = email
          self.address = address

    def show(self):
        print("--------Customer--------")
        print("{} | {}".format(self.name, self.phone))
        print("{} | {}".format(self.email, self.address))
        print("------------------------")


# 1 Order can have many dishes
# 1 Order can have 1 customer
class Order:

    def __init__(self, oid=0, dishes=None, customer=None, total=0):
          self.oid = oid
          self.dishes = dishes
          self.customer = customer
          self.total = total

    def show(self):
        print("--------Order--------")
        print("{} | {}".format(self.oid, self.total))
        print("--------------------")

        print("Order Placed By:")
        self.customer.show()

        print("--------Order Dishes--------")
        for dish in self.dishes:
             dish.show()
        print("----------------------------")

    def link_dishes(self, dishes):
        self.dishes = dishes

        for dish in self.dishes:
            self.total += dish.price

    def link_customer(self, customer):
        self.customer = customer

from resturant_dish import Dish
from session11 import Customer

dish_menu = [
          Dish(name="Dal Makhani", price=250, rating=4.5), 
          Dish(name="Paneer Makhani", price=400, rating=4.2), 
          Dish(name="Noodles", price=300, rating=3.5), 
          Dish(name="Pizza", price=650, rating=4.0), 
          Dish(name="Burger", price=50, rating=3.1)
          ]

customer1 = Customer(name="John", phone="+91 99999 11111", email="john@example.com", address="Redwood Shores")
customer2 = Customer(name="Fionna", phone="+91 99999 22222", email="fionna@example.com", address="Country Homes")

# Hard Coding: We as developer are linking objects
# order1 = Order(oid=1, dishes=[dish_menu[0], dish_menu[2]], customer=customer1, total=550)
# order2 = Order(oid=2, dishes=[dish_menu[2], dish_menu[3], dish_menu[4]], customer=customer1, total=1000)

order1 = Order(oid=1)
order1.link_customer(customer=customer1)
order1.link_dishes(dishes=[dish_menu[0], dish_menu[2]])

order2 = Order(oid=2)
order2.link_customer(customer=customer1)
order2.link_dishes(dishes=[dish_menu[2], dish_menu[3], dish_menu[4]])

order1.show()
order2.show()