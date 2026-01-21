#1 

try:
    num = int(input("enter a number: "))
    print(num)
except:
    print("the input is not a number")

#2
try:
    list = ["red", "blue", "yellow"]
    print(list[4])
except IndexError:
    print("index does not exist")

#3

try:
    int("something")
except TypeError:
    print("who is this pokemon?!")

