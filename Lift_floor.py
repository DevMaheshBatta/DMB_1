floors=10
floor=0
floortogo=int(input("enter floor number to go"))

while floor<=floors:
    print("at floor:",floor)
    if floortogo ==floor:
        print("you have to reached at floor number",floor)
        break
    floor +=1
    
