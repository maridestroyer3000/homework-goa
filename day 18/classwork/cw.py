# n1
mixed_list = [25, 7, "hello", "world", 3.14, 2.71, True, False]

# n2
integers = [x for x in mixed_list if type(x) == int]
strings = [x for x in mixed_list if type(x) == str]
floats = [x for x in mixed_list if type(x) == float]
booleans = [x for x in mixed_list if type(x) == bool]

# n3
print("Integers:", integers)
print("Strings:", strings)
print("Floats:", floats)
print("Booleans:", booleans)