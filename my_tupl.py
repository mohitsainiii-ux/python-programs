def square_tuple():
    my_list = list()

    for i in range(1, 21):
        my_list.append(i ** 2)

    my_tuple = tuple(my_list)
    print(my_tuple)

square_tuple()