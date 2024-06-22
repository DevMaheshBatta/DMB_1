import random

"""
1 for snake
-1 for water
0 for gun

"""
computer=random.choice([-1,0,1])
youstr=input("Enter Your Choice: ")
youdict={"s":1 ,"w":-1,"g":0 }
reversedict={1:"Snake",-1:"Water",0:"Gun"}
you=youdict[youstr]
print(f"you Chose {reversedict[you]}\n  computer chose {reversedict[computer]} \n")
if (computer==you):
    print("You are Draw")

elif( computer==-1 and you==1):
          print("You Win!")


elif(computer==-1 and you==0):

 print("You Loose!")

elif(computer==1 and you==-1):
 print("You Loose!")

elif(computer==1 and you==0):
 print("You Win!")

elif(computer==0 and you==-1):

 print("You Win")

elif(computer==-1 and you==1):
 print("You Loose")
else:
 print("Something Went Wrong ")
 