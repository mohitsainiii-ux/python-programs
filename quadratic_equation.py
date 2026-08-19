import math

def quadratic(a, b, c):
    d  = b * b -4 * a * c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2

    elif d == 0:
        x = -b / (2 * a)
        return x

    else:
        return "No Real roots"

a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))

result = quadratic(a,b,c)

print("Roots : ", result)