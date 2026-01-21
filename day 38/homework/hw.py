car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))


x = {'type' : 'fruit', 'name' : 'banana'}
print(x['type'])

# it will print fruit


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020


x = {'type' : 'fruit', 'name' : 'banana'}
x.update({'name' : 'apple'})


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"


x = {'type' : 'fruit', 'name' : 'apple'}
x.update({'color' :'green'})


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()


myvar = {'type' : 'fruit', 'name' : 'apple', 'color' : 'red'}
del myvar['color']


myset = {'apple', 'banana', 'cherry'}
for x in myset:
  print(x)


a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
print(customers['c2']['name'])


a = {'name' : 'John', 'age' : 20}
b = {'name' : 'May', 'age' : 23}
customers = {'c1' : a, 'c2' : b}
for x, obj in customers.items():
  print(x)
    
  for y in obj:
    print(y + ':', obj[y])


a = 50
b = 10
if a > b:
  print("Hello World")


a = 50
b = 10
if a !=b:
  print("Hello World")

  if 5 > 2:
    print("YES")