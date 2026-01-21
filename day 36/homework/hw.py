def count_by(x, n):
    return [i * x for i in range(1,n+1)]

def summation(num):
     return sum([n for n in range(num+1)])

def square_sum(numbers):
    return sum([num*num for num in numbers])

def invert(lst):
    return [n * -1 for n in lst] if len(lst) > 0 else []

def greet():
    return "hello world!"

def solution(string):
    return string[::-1]

def find_smallest_int(arr):
    return min(arr)

def string_to_number(s):
    return int(s)

def remove_char(s):
    return s[1:-1]

def repeat_str(repeat, string):
    return repeat * string

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
            
    return sum

def opposite(number):
    return number * (-1)

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def make_negative( number ):
    if number <= 0:
        return number
    else:
        return number *(-1)
    
def number_to_string(num):
    return str(num)

def make_upper_case(s):
    x = s.upper()
    return(x)

def multiply(a, b):
    return a * b

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else: 
        return 0
    

