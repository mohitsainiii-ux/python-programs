numbers = [5, 6, 77, 45, 22, 12, 24]

def remove_even_numbers():
    result = [num for num in numbers if num % 2 != 0]
    print(result)

remove_even_numbers()