john_followers={"fionna","sia","jack","joe","george","kia"}
print(john_followers)
print(type(john_followers))
print(len(john_followers))

numbers=list(range(10,101,10))
numbers1=set(numbers)
print("numbers",numbers)
print("numbers1",numbers1)

numbers1.add(101)
numbers1.add(201)
numbers1.add(301)
print("numbers1 is:",numbers1)
numbers1.remove(90)
numbers1.remove(30)
numbers1.remove(101)
numbers1.discard(201)
print("2.numbers1:",numbers1)


john_followers={"fionna","sia","jack","joe","george","kia"}
jake_followers={"anna","sia","kai"}
fionna_followers = {"sia", "joe"}

mutual_followers = john_followers.intersection(jake_followers)
print(mutual_followers)

result = fionna_followers.issubset(john_followers)
print("result is:", result)

result = john_followers.issuperset(fionna_followers)
print("result is:", result)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Error
# C = A + B
# print("C is:", C)

D = A - B
print("D is:", D)

E = A ^ B
print("E is:", E)

F = A | B
print("F is:", F)


A.clear()
print("A is:", A)
print("Length of A is:", len(A))

# Create an Empty Set
my_set = set()
my_list = []
my_dict = {}
my_tupple=()
my_dict={}
my_dict=dict



# Explore Dictionary/Map/JSON

my_data = {
    101: "John",
    201: "Jennie",
    501: "Sia",
    99: "Joe",
    25: "Kim",
    201: "Anna"
}

# my_data = {
#     "jo": "John",
#     "je": "Jennie",
#     "si": "Sia",
#     "ji": "Joe",
#     "ki": "Kim"
# }

print("my_data")
print(my_data)

print(len(my_data))
print(min(my_data))
print(max(my_data))
print(sum(my_data)) # -> works only for int keys

print(my_data[201])
print(my_data.get(201))

my_data.pop(25)
# del my_data[25]

my_data[99] = "Joseph"
print(my_data)

attendance = ["june", "july", "aug", "july"]
college_attendance = {}.fromkeys(attendance, 100)
college_attendance["aug"] = 70
print(college_attendance)


items = list(my_data.items())
values = list(my_data.values())

print(items)
print(values)

for item in my_data.items():
    print(item)

for value in my_data.values():
    print(value)

