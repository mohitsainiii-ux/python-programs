import random

def generate_even_numbers():
    even_nums = list(range(100, 201, 2))
    result = random.sample(even_nums, 5)
    return result

print(generate_even_numbers())