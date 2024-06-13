
#containers
#single value container
username="auribises"#reference variablefor containner
promo_code="abc"#snakecase
print(username,id(username))#print is read statement
username=("abc")
print(username,id(username))
#adress is hash code
del username

promocode1="zomato"
print(promocode1,type(promocode1),id(promocode1))
#reference copy operation
promocode2=promocode1
print(promocode2,type(promocode2),id(promocode2))
del promocode1
print(promocode2,type(promocode2),id(promocode2))
#----------------------------------------------------

friends=("jon","jam","jim")   #tuple can not be changed ,once created 
print (friends,type(friends))
print(friends[0],type (friends[0]),id (friends[0]))
print(friends[1],type( friends[1]),id (friends[0]))
print(friends[2],type( friends[2]),id (friends[0]))
#----------------------------------------------------
friends=["jon","jam","jim"]   # list it can be changed
print (friends,type(friends))
numbers=[10,20,30,40,40]
print(numbers,type(numbers),id(numbers))
mynumbers=numbers
print(mynumbers,type(mynumbers),id(mynumbers))
numbers[2]=1122
print(numbers[2])
print(mynumbers[2])
del numbers
print(mynumbers)
#-----------------------------------------------------
#hashing
number={10,20, 30,30,40,50} #set duplicate not allowed in set
#cant not change set
print(number,id(number),type(number))
number1=[10,10,20,30,40]     #duplicate posiible
print(number1,id(number1),type(number1))
johnfriends={"joe","jim","fionna","harry","kim","joe"}
siafriends={"joe","george","leo","jack","ben","jack"}
mutualfriends=johnfriends&siafriends
print(mutualfriends)
#dictionary--------------------------------------------
friend={"jj":"john","je":"jennie","ji":"jim"}
print(friend)
instagram={"dev":{"auri","john","jenni"},
"ankit":{"george","sia","leo"}
}
print(instagram["dev"])
name=(input("enter name"))
print("name is",name)
age=int(input("enter age"))
print("age is",age)

