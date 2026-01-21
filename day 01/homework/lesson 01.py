name = "mari"
#name არის ცვლადი
# = არის ცვლადისთვის მიმნიჭებელი სიმბოლო
# "mari" არის ცვლადისთვის მნიშვნელობდა

surname = "surguladze"

# print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "mari" #ეს არის str (string) ტიპის ცვლადი
age = 15 # ეს არის int (integer) მთელი რიცხვი
height = 166 #ეს არის float ტიპის ცვლადი ( ათწილადი )
#boolean (bool) ტიპის ცვლადი

knows_programming = True  #True ან False
is_ugly = False #snakecase(უბრალოდ წერის სტილი სტანდარტულად)

isUgly = False # ჯავასკრიპტული camelcase


# print(name + " " + surname)

# #სტრინგი არის ბრჭყალებშ მოქცეული სიმბოლოები
# print(name + age)

# print(type(age))
# print(type(name))
# print(type(surname))
# print(type(height))
# print(type(knows_programming))

print(name + " " + str(age) + surname + int(height))