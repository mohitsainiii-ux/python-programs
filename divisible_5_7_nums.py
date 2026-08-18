import random

def generate_numbers():
    nums = [ i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0]
    return random.sample(nums, 5)

print(generate_numbers())