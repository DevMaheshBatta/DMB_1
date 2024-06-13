instagram_user_name=["john.j","fionna","harry_h","leo.32","ben"]
names=["john jackon,finna,","harrison","leonardo","bennethan"]
username=input("enter username to search")

idx=0
while idx<len(instagram_user_name):
    if username==instagram_user_name[idx]:
        print("name is",names[idx])
        break
        
    idx+=1

flag =False     
for idx in range(0,len(instagram_user_name)):
     print("check",username,"with",instagram_user_name[idx])
     if username==instagram_user_name[idx]:
        print("name is",names[idx])
        flag =True
        break
     if flag==False:
        print(username,"not found")
        #------------------------------------------------------------