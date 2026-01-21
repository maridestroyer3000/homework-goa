def multiply(a, b):
    return a * b

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def number_to_string(num):
    return str(num)

def make_negative( number ):
    if number <= 0:
        return number
    else:
        return number *(-1)
    
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
def opposite(number):
    return number * (-1)

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
            
    return sum

def repeat_str(repeat, string):
    return repeat * string

def remove_char(s):
    return s[1:-1]

def string_to_number(s):
    return int(s)

def no_space(x):
    return x.replace(" ", "")