# *rest გამოიყენება ფრჩხილებში მოცემული მნიშვნელობის პრინტისას, დანარჩენი მონაცემების გამოსაყვანად ტერმინალში

#1

names = ("Gio", "Nika", "Alex", "Deme", "Luka")

name1 , *name = names

print(name)

#2

colors = ("blue", "yellow", "green", "pink", "red")

color2 , *color = colors
print(color)

#3

foods = ("xinkali", "pizza", "xachapuri", "mwvadi",)

food3 , *food = foods

print(food)

# it bothers me that foods doesnt exist but whatever

#4

series = ("lost", "breaking bad", "dexter", "you", "2 broke girls")

serie4 , *serie = series

print(serie)

#5

mcdonalds = ("nuggets", "cheeseburger", "happy meal", "big mac", "fries", "bbq sauce")

mcdonald5 , *mcdonald = mcdonalds

print(mcdonald)

# tuple არის კოლექციის ტიპი, რომელიც თანმიმდევრულია, მაგრამ ლისტისგან განსხვავებით არცერთი ელემენტის შეცვლა არ შეგვიძლია

#1

numbers = ("one", "two", "three", "six", "seven", "nine")

x = numbers.index("nine")

#2

veggies = ("cucumber", "tomato", "carrot", "potato", "broccoli", "garlic")

x = veggies.count("tomato")