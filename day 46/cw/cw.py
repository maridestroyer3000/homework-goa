# 1

try:
    print("nini")
except:
    print("something went wrong")

#2 

try:
    age = 17
    print(city)
except NameError:
    print("not defined")
    

#3

try: 
    print(len(1))
except IndexError:
    print("incorrect")
except TypeError:
    print("this is wrong")

#4

try: 
    str(True)
except ValueError:
    print("something went wrong")

#5

try: 
    birds = ["parrot","crow", "eagle"]
    print(birds[6])
except IndexError:
    print("invalid index")
    

#6

try: 
    print(len(12))
except: 
    print("aint right")

#7 

try: 
    int(34.2)
except:
    print("invalid value")

#8

try:
    height = 183
    print(gender)
except:
    print("undefined")

#9 
try: 
    print("sober)"
except:
    print("went wrong")


#10

try: 
    print('no)
except SyntaxError:
    print("incorrect syntax")




# SyntaxError არასწორი სინტაქსი print(nika")
# NameError ცვლადი არ არის სწორი/არ არსებობს age = 15 print(city)
# IndexError მითითებული ინდექსი არის რაოდენობაზე მეტი count = ["name"] print(count[2])
# TypeError არასწორი არგუმენტი (len(4))
# ValueError არასწორად მითითებულია კოდი (მაგალითად str(4))