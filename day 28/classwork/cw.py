# tuple შეუცვლელია, მასში შესულ მონაცემებს ვერ შეცვლი, ხოლო listში მოცემული მონაცემების შეცვლა შესაძლებელია.

animals = ("dog", "cat", "parrot", "mouse", "hamster")

animal1, *animal = animals

print(animal)