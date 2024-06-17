"""
principle of oops
1.Think of an objects
login page : name,email,aadhar ,otp ,gender 



"""
#create class of object
#below class represents the object .it is description of object

class loginpage:
    pass

#create the real object in memory
#below  is object construction statement

login1=loginpage()
#booking is reference variable ,flightbooking()-represent the object construction
print(login1)
print(id(login1))
print (hex(id(login1)))
login2=loginpage()
#write operation 
login1.name="shivam"
login1.email="shivam12@hgmail.com"
login1.aadhar="23348494940"
login1.gender="male"
login1.phone="8360924774"

#------------------------
login2.name="Dev"
login2.email="shivam32@hgmail.com"
login2.aadhar="23548494940"
login2.gender="male"
login2.phone="8360924374"
login2.otp="23333"
#updatelogin1
login1.email="shivam21@gmail.com"

#read data
print("login no1 ")
print(vars(login1))
print("Name:",login1.name ,"gender",login1.gender)
print("login no2")
print(vars(login2))
print(" Name:",login2.name,login2.email)
#delete operation
del login1.aadhar
print("login1 data:")
print(vars(login1))
del login1



