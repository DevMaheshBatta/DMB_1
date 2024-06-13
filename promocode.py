""" Zomato:20% off
          :minvalue:300   

      Bingo :50%off
            :minvalue:500
            :max discount:100  """
promocode= input("enter promo code:")
amount= float(input("enter amount"))
if promocode=="ZOMATO":
    print( "ZOMATO is Applied")
    if amount>300:
        discount=0.20*amount
        print("zomato applied sucessufully",discount)
        print("you can pay",amount-discount)
    else:
        print("amount is lees .please add  item worth",(300-amount),"more")
elif promocode=="BINGO":
     print("Bingo can be applied")
     if amount>500:
         discount=0.50*amount
         if discount>100:
             discount=100
             print("bingo applied sucessfully. you got a discount of",discount)
             print("you can pay:\u20b9",amount-discount)
         else:print("amount is less .please add item worth ",500-amount,"more")
     else:print("invalid promocode")

