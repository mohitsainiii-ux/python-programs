def tuple_gen():
    t = (1, 2, 3, 4, 5,6 , 7, 8, 9, 10)

    for i in range(len(t)):
        if t[i] % 2 == 0:
            print(t[i])

tuple_gen()