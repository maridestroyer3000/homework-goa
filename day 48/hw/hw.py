#1
def odd_or_even(arr):
    total = sum(arr)
    return "even" if total % 2 == 0 else "odd"

#2
def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b: 
        return True
    else:
        return False

#3
def get_count(sentence):
    count = 0
    
    vowels = "aeiou"
    
    for i in sentence.lower():
        if i in vowels:
            count += 1
    return count

#4
def fizzbuzz(n):
    new_list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            new_list.append("FizzBuzz")
        elif i % 3 == 0:
            new_list.append("Fizz")
        elif i % 5 == 0:
            new_list.append("Buzz")
        else:
            new_list.append(i)
    return new_list

#5
def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return f"{nums[-1]} {nums[0]}"

#6
def number(lines):
    return [f"{i}: {line}" for i, line in enumerate(lines, 1)]

#7
def row_sum_odd_numbers(n):
    return n**3

#8
def filter_list(l):
    return [x for x in l if isinstance(x, int)]

#9
def get_middle(s):
    length = len(s)
    mid_index = length // 2
    if length % 2 == 1:
        return s[mid_index]
    else:
        return s[mid_index - 1:mid_index + 1]
    
#10
def find_short(s):
    lengths = [len(word) for word in s.split()]
    return min(lengths)