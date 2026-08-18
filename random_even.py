import random

def random_even():
    even_numbers = [num for num in range (0, 11) if num % 2 == 0]
    return random.choice(even_numbers)

print(random_even())