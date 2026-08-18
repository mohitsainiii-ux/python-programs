import random

def random_numbers():
    numbers = random.sample(range(100, 201), 5)
    return numbers

print(random_numbers())