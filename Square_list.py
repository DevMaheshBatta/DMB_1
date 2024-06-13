def square(num):
    print("1 .num is:",num,id (num))
    num*=num# num=num*num
    print("2.mum is ",num,id(num))
    return
number=10
print("A.number is:",number,id (number))
square(number)
print("B.  number is",number,id (number))



def squareofnumbers(nums):
    print("1 .num is:",nums)
    for idx  in range(0,len(nums)):
        nums[idx]=nums[idx]*nums[idx]
    print("2.num is ",nums ,id(nums))
    return
numbers=[10,20,30,40,50]
print("A.number is:",numbers,id (numbers))
squareofnumbers(numbers)
print("B.  number is",numbers,id (numbers)) 