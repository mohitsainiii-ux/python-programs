def check_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

number = int(input("ENter a number : "))

if check_prime(number):
    print("The number is prime")
else:
    print("the number is not prime")