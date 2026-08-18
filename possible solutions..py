def find_animals():
    heads = 35
    legs = 94

    for chicken in range(heads + 1):
        rabbits = heads - chicken

        if (chicken * 2) + (rabbits * 4) == legs:
            print("Number of Chickens : " , chicken)
            print("Number of Rabbits : ", rabbits)

find_animals()