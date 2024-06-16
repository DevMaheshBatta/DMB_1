amount=int(input("Enter amount you want to take debt "))
first_installament = ( 0.10* amount)
print ("first installement  is :",first_installament)
pending=(amount-first_installament)
amount_to_pay=(0.15*pending)+(pending)
print ("amount to pay is:",amount_to_pay)

max_amount_coustmer=int(input("enter amount U can pay in one month it should be >5000::"))
month=amount_to_pay//max_amount_coustmer
which_monthstarted=int(input("enter month loan started"))
print("month to end loan",which_monthstarted+month)
