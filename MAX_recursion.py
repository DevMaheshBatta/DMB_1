def get_max(data,length):
    if length==1:
        return data[0]
    else:
        previous=get_max(data,length-1)
        current=data[length-1]
        
        if previous>current:
            return previous
        else:
            return current
    

number=[1,5]
max=get_max(number,len(number))
print("max: is ",max)
