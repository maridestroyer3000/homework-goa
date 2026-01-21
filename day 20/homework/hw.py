# n1
string = "play"
if string[0].isupper():
    print(string.upper())
else:
    print(string.lower())

# n2
name = input("enter your name: ")
has_upper = False
for char in name:
    if char.isupper():
        has_upper = True

if has_upper:
    print(name.lower())

else:
    print(name.capitalize())

# n3
animals =  ["Dog" , "Cat", "Tiger", "Fox", "Wolf"]
if len(animals) < 5 and animals[0].isupper():
    print(animals[:3])
else:
    print(animals, "long")

# n4
names = ["achi", "mari", "taso", "gio"]
for name in names:
    print(name.upper())

# n5
types = ["string", 1, True, 2.3, False]
for item in types:
    if type(item) == str:
        upper_str = item.upper()
        print(upper_str[-3:])

