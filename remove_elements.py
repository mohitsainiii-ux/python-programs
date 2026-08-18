def remove_elements(numbers):
    result = [
        value
        for index, value in enumerate(numbers)
        if index not in (0, 4, 5)
    ]
    return result
numbers = [12, 24, 35, 70, 88, 120, 155]
new_list = remove_elements(numbers)
print("Original list:", numbers)
print("After removing elements:", new_list)