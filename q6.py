import math

C = 50
H = 30

D = input("Enter values: ").split(",")

result = []

for value in D:
    value = int(value)

    Q = math.sqrt((2 * C * value) / H)

    result.append(round(Q))

print(",".join(map(str, result)))