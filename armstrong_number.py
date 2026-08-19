def arm_num(num):
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print("Armstrong")
    else:
        print("Not Armstrong")

number = int(input("Enter Number : "))
arm_num(number)