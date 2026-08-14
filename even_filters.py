def even_filter():
    even_num = list(filter(lambda x: x % 2 == 0, range(1, 21)))
    print(even_num)
even_filter()