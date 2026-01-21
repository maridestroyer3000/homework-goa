only_even = [n for n in range(1, 11) if n % 2 == 0]
           
print(only_even)

squares =[y * y for y in range(1, 11)]

print(squares)

fruits = ["apple", "banana", "cherry", "date"]
fruits = [fruit.capitalize() for fruit in fruits]

print(fruits)

animals = ["cat", "dog", "elephant", "mouse"]
animals = [len(animal) for animal in animals]

print(animals)



num = [5, 12, 8, 20, 3, 15]
num = [n for n in num if n > 10]

print(num)


numbers = [1, 2, 3, 4]
numbers = [numbers * 5 for numbers in numbers]

print(numbers)


words = ["hello", "world", "python", "programming", "list"]
words = [word for word in words if word.startswith('p')]

print(words)



numb = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_nums = [i for i in numb if i % 2 == 0]

odd_nums = [i for i in numb if i % 2 != 0]

for i in numb:
    if i % 2 == 0:
        even_nums.append(i)
    else:
        odd_nums.append(i)

print(even_nums)
print(odd_nums)
