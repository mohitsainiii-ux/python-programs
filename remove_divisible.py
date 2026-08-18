numbers = [12, 24, 35, 70, 88, 120, 155]

def remove_5_7_divisible():
    result = [num for num in numbers if num % 5 != 0 and num % 7 != 0]
    print(result)

remove_5_7_divisible()