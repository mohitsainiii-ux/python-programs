numbers = [12, 24, 35, 70, 88, 120, 155]

def remove_even_index():
    result = [value for index, value in enumerate(numbers) if index % 2 != 0]
    print(result)

remove_even_index()