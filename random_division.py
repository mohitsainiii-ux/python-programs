import random

def random_division():
    division_numbers = [num for num in range(201) if num % 5 == 0 and num % 7 == 0]
    return random.choice(division_numbers)

print(random_division())