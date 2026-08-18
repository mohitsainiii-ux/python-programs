def remove_duplicates(numbers):
    seen = set()

    result = [value for value in numbers if not (value in seen or seen.add(value))]

    return result
numbers = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
new_list = remove_duplicates(numbers)
print("Original list:", numbers)
print("After removing duplicates:", new_list)
