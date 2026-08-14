numbers = input("Enter numbers : ")
numbers = [int(x) for x in numbers.split(",")]
odd_numbers = [x for x in numbers if x % 2 != 0]
squared_numbers = [x ** 2 for x in odd_numbers]
print("Odd numbers: ", ", ".join(map(str, odd_numbers)))
print("Squared odd numbers: ", ", ".join(map(str, squared_numbers)))