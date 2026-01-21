# მომხმარებელს შემოატანინეთ მისი ასაკი და გაიგეთ რამდენჯერ მოთავსდება რიცხვი 10 მასში

age = int(input("enter your age: "))
print(age // 10)

# მომხმარებელს შემოატანინეთ მისი სახელი და გაიგეთ უდრის თუ არა ის თქვენს სახელს

name = int(input("enter your name: "))
my_name = "mari"
print(name == my_name)

# მომხმარებელს შემოატანინეთ ორი რიცხვი (num1 და num2) და გაიგეთ რა იქნება ნაშთი, პირველი რიცხვის მეორეზე გაყოფის შემდეგ

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
print(num1 % num2) 

# მომხმარებელს შემოატანინეთ მისი ასაკი და გაიგეთ არის თუ არა ის ლუწი (იყოფა თუ არა ზუსტად 2ზე) ანუ გვრჩება თუ არა ნაშთი ნული, ორზე გაყოფის შედეგად

your_age = int(input("enter your age: "))
print(your_age % 2 == 0)
