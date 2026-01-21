# list comprehension გვჭირდება, რომ შევამოწმოთ ელემენტი პირობის მიხედვით და კოდის შესამოკლებლად.

nums = [3, 6, 12, 24, 64, 44, 71, 83, 19, 11]

num1 = [i for i in nums if i % 3 == 0 and i % 5 == 0]

print(nums)
print(num1)

names = ["gia", "saba", "nuca", "nita", "ele", "toko", "deme", "gio"]

even_names = [i for i in names if len(i) % 2 == 0]

print(even_names)