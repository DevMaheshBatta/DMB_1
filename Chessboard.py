black_pawn="\u265F" 
black_square = "\u25A0"
black_rook="\u2656"
black_Knight="\u2658"
black_bishop="\u2657"
black_king="\u2658"
balck_queen="\u2655"
white_rook="\u265C"
white_pawn="\u2659"
white_square = "\u25A1"
white_knight="\u265E"
white_bishop="\u265D"
white_queen="\u265B"
white_king="\u265E"
for i in range(0,1): 
    for j in range(0,8):
        if j ==0 or j==7:
            print(white_rook,end=" ")
        if j ==1:
            print(white_knight,end=" ")
        if j ==2:
            print(white_bishop,end=" ")
        if j ==3:
            print(white_queen,end=" ")
        if j ==4:
            print(white_king,end=" ")
        if j ==5:
            print(white_bishop,end=" ")
        if j ==6:
            print(white_knight,end=" ")
        # if j ==7:
            # print(white_rook,end=" ")  

    print()       

    
   
    
for i in range(1,2):
    for j in range(0,8):
     print(black_pawn,end=" ")

    print()

for i in range(2, 6): # 0, 1, and 3
    # print("i is:", i)

    for j in range(0, 8): # 0, 1, 2, 3, 4
        # print(j, end=" # ")

        if i % 2 == 0:
            # print(j%2, end=" ")
            if j%2 == 0:
                print(black_square, end=" ")
            else:
                print(white_square, end=" ")
        else:
            # print((j+1)%2, end=" ")
            if (j+1)%2 == 0:
                print(black_square, end=" ")
            else:
                print(white_square, end=" ")

    print()   


        

for i in range(7,8):
    for j in range(0,8):
     print(white_pawn,end=" ")

    print()

for i in range(0,1):
    for j in range(0,8):
        if j ==0:
            print(black_rook,end=" ")
        if j ==1:
            print(black_Knight,end=" ")
        if j ==2:
            print(black_bishop,end=" ")
        if j ==3:
            print(black_king,end=" ")
        if j ==4:
            print(balck_queen,end=" ")
        if j ==5:
            print(black_bishop,end=" ")
        if j ==6:
            print(black_Knight,end=" ")
        if j ==7:
            print(black_rook,end=" ")  

    print()  
