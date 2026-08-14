from operator import itemgetter

data = input("Enter data : ").split()
tuples = []
for item in data:
    name, age, score = item.split(",")
    tuples.append((name, age, score))
result = sorted(tuples, key=itemgetter(0, 1, 2))
print(result)