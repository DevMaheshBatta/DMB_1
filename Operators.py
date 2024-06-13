#operators
#Arthmetic operators
#  +,-,*,**,/,//,%
prouductprice=200
gsttax=0.18
pricetopay=prouductprice+gsttax*prouductprice
print(pricetopay,type(pricetopay)),id(pricetopay)






bucketsize=7
hashcode=120%bucketsize
age=20
print("r")
#update operation
#age=age+10
age+=10
age %=3
age -=1
print("age now is:",age)
#increment and decrement
qty=1
qty +=1
qty -=1
qty +=5
qty -=1
qty **=2 #5 raise to pawer 2
# conditional operators
# ==,!=,<,>,>=,<=
cabfare=500
ewallet=500
result=ewallet>=cabfare
print("can i run",result)
print(type(result))
email=input("enter email")
password=input("enter password")
print("is login sucess??")
result=(email=="john@example.com") and(password=="john123")
print(result)
otp=3027
userotp=int(input("enter otp received"))
print("is otp correct",otp==userotp)
# membership testing
#is not
a=10
b=10
print(a==b)#true
print(a is b)# true
print(a is  not b)# false



#----------------------------------------------------------------
speed=60
time=9
speed=speed*(5//18)
length=speed*time
print("length of train", length)

# find 5 quantative appitude problenm solve using operators
