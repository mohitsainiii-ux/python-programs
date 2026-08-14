def square_number():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squared_num = list(map(lambda x: x**2, numbers))
    print(squared_num)

square_number()