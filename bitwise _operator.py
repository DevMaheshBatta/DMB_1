#bitwise operator
# &,|,^
num1=10 #1010
num2=8  #1000
print ("num1 in binary ",bin(num1))
print("num2 in binary",bin(num2))
result1=num1& num2 
result2=num1|num2
result3=num1^num2
print("result",result1)
print("result2",result2)
print("result3",result3)
 #shift operator
num3=8
num4=2
result4=num3>>num4
print("result right ",result4)

result5=num3<<num4
print("result right ",result5)









#-----------------------------------
amount=float(input("enter amount:"))
promocode=input("enter promo code")
if promocode=="zomato":
    Print ("valid promo code")
    if amount>249:
        print("promocode zomato is applied") 
        discount=0.50*amount
        if discount>=150:
           discount=150
           amount -=discount
           print (discount)
    
    else:print("amount is low")

else:print("promo code invalid")
