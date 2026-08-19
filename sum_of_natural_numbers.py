def sum_natural_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


number = int(input("Enter a number: "))

print("Sum of natural numbers is:", sum_natural_numbers(number))
