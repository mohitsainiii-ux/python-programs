X, Y = input("Enter X,Y: ").split(",")

X = int(X)
Y = int(Y)

array = []

for i in range(X):
    row = []

    for j in range(Y):
        row.append(i * j)

    array.append(row)

print(array)