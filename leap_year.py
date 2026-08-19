def check_leap_year(num):
    if num % 4 == 0 or num % 400 == 0:
        print("Leap Year")
    else:
        print("Non Leap Year")

number = int(input("Enter A Year : "))
check_leap_year(number)