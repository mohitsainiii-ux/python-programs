import itertools

def print_permutations(numbers):
    result = itertools.permutations(numbers)

    for permutation in result:
        print(permutation)

numbers = [1, 2, 3]
print_permutations(numbers)