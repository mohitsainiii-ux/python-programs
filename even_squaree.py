def even_square():
    s1 = [1,2,3,4,5,6,7,8,9,10]
    even_num = list(map(lambda x: x ** 2, filter (lambda x: x % 2 == 0, s1)))
    print(even_num)

even_square()