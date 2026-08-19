def area_of_triangle(base, height):
    return 0.5 * base * height

base = float(input("Enter base : "))
height = float(input("Enter Height : "))

area = area_of_triangle(base, height)

print("Area Of Triangle : ", area)