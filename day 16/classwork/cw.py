# 1) while ციკლის გამოყენებით გამოიტანეთ 1 დან 20 მდე ყველა რიცხვი
num = 1
while num <= 20:
    print(num)
    num += 1

# 2) შექმენით ცვლადი რომელშიც შენახული იქნება პინ კოდი მაგ:1234 
# და მომხმარებელს შემოაყვანინეთ პინ კოდი, სანამ არ დაემთხვევა ორიგინალს
correct_pin = "1234"
entered_pin = input("enter pin code: ")

while entered_pin != correct_pin:
    print("pin code is wrong. try again.")
    entered_pin = input("enter pin code: ")

print("პინ კოდი სწორია!")

# 3) for ციკლის საშუალებით 1 დან 20მდე დაპრინტეთ ყველა ლუწი რიცხვი
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 4) for ციკლის საშუალებით 1 დან 30 მდე დაპრინტეთ ყველა კენტი რიცხვი
for i in range(1, 31):
    if i % 2 != 0:
     print(i)

# 5) while ციკლის საშუალებით 1 დან 10მდე დაპრინტეთ ყველა ლუწი რიცხვი
n = 1
while n <= 10:
    if n % 2 == 0:
        print(n)
    n += 1
