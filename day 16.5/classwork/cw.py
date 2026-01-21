# მომხმარებელს შემოატანინეთ სახელი
name = input("emter your name: ")

# for ციკლის საშუალებით დაბეჭდეთ თითოეული ასო
for letter in name:
    print(letter)

# for ციკლი 1-დან 30-მდე
for i in range(1, 31):
    if i % 2 == 0:
        print(f"{i} ლუწია")
    else:
        print(f"{i} კენტია")
