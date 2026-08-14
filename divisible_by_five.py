def divisible_by_five(numbers):
    result = []

    for number in numbers:
        number = number.strip()

        decimal = int(number, 2)

        if decimal % 5 == 0:
            result.append(number)

    return result


numbers = input("Enter binary numbers: ").split(",")

result = divisible_by_five(numbers)

print(",".join(result))