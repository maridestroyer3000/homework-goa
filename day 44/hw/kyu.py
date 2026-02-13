#1
def invert(lst):
    if len(lst) > 0:
        return[x * -1 for x in lst] 
    else:
        return []
    
#2
def positive_sum(arr):
    sum = 0 
    
    for i in arr:
        if i > 0:
            sum += i
            
    return sum

#3
def count_by(x, n):
    return [i * x for i in range(1,n+1)]

#4
def summation(num):
    return sum([n for n in range(num+1)])
    
#5
def square_sum(numbers):
    return sum([num*num for num in numbers])
        
# 6
def greet(name):
    return "Hello, {} how are you doing today?".format(name)

# 7
def greet():
    return "hello world!"

# 8
def solution(string):
    return string[::-1]
    
# 9
def find_smallest_int(arr):
    return min(arr)

# 10
def string_to_number(s):
    return int(s)

# 11
def remove_char(s):
    return s[1:-1]

# 12
def repeat_str(repeat, string):
    return repeat * string

# 13def opposite(number):
    return number * (-1)

# 14
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"

# 15
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# 16
def make_negative( number ):
    if number <= 0:
        return number
    else:
        return number *(-1)
    
# 17
def number_to_string(num):
    return str(num)

# 18
def make_upper_case(s):
    x = s.upper()
    return(x)

# 19
def multiply(a, b):
    return a * b

# 20
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else: 
        return 0