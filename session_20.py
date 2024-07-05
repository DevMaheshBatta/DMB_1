# String in Action
# Textual Data Type

name = 'John'
cafe_name = "John's Cafe"

# Multi Line String
message = """Hi
How Are you..
This is John from John's Cafe
"""

# Raw String -> Accepts special characters as data
# Regular Expression uses Raw String :)
cafe_name = r'John\'s \nCafe'

print(name)
print(cafe_name)





# Properties
"""
    Indexing
    Negative Indexing
    Slicing
    Concatenation
    Multiplicity
    Membership Testing
"""

quote = "search the candle rather than cursing the darkness"
print("1. HashCode of Quote:", id(quote))

print(quote[1])
print(quote[-1])
print(quote[-8:])

quote = quote + "\n" + "Be Exceptional\n"
print(quote)
print("2. HashCode of Quote:", id(quote))

data = quote * 3
print("`````````````````")
print(data)
print("`````````````````")

print("the" in quote)

email = input("Enter Your Email: ")
if "@" in email and "." in email:
    print("Email is Well Formed:", email)
else:
    print("Email is NOT Well Formed:", email)


contacts = ["john", "jennie", "kia", "joe", "jackson", "anna", "sia"]
search = input("Enter Search keyword: ")
for contact in contacts:
    if search in contact:
        print(contact)







# Strings are IMMUTABLE -> THEY CANNOT BE CHANGED

quote = "be exceptional"
print("HashCode of quote is:", id(quote))
s1 = quote.upper()
print("1. Quote is:", quote)
print("1. HashCode of quote is:", id(quote))

s2 = quote.lower()
print("2. Quote is:", quote)
print("2. HashCode of quote is:", id(quote))

print("s1 is:", s1)
print("s2 is:", s2)

s3 = quote.capitalize()
print("s3 is:", s3)

s4 = quote.title()
print("s4 is:", s4)

quote = "Be Exceptional"
s5 = quote.swapcase()
print("s5 is:", s5)