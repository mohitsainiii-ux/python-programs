def swap_two_variables(a,b):
    a, b = b, a
    return a,b

a = int(input("Enter first number : "))
b= int(input("Enter second number : "))

a,b = swap_two_variables(a,b)

print("After Swapping : ")
print("A = ", a)
print("B = ",b)