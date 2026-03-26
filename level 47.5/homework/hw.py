def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def get_min_max(seq): 
    return min(seq), max(seq)

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])