dictionary = {

    "name": "Mari",
    "age": 15,
    "city": "Tbilisi"

}
dictionary.pop("name")

dictionary["age"] = 16

for i in dictionary.values:
    print(i)

user_age = dictionary.get("age")
print(user_age)
