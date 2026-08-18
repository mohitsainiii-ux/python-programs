subject = ["I", "YOU"]
verb = ["Play", "Love"]
object = ["Hockey", "Football"]

def generate_sentences():
    for i in range(2):
        for j in range(2):
            for k in range(2):
                print(subject[i], verb[j], object[k])

generate_sentences()