def generate_dictionary():
    my_dict = {}

    for i in range(1, 21):
        my_dict[i] = i ** 2
    for i in my_dict.keys():
        print(my_dict[i])

generate_dictionary()