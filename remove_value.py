def remove_value(numbers):
    # Remove all occurrences of 24 using list comprehension
    result = [value for value in numbers if value != 24]
    return result
numbers = [12, 24, 35, 24, 88, 120, 155]
new_list = remove_value(numbers)
print("Original list:", numbers)
print("After removing 24:", new_list)