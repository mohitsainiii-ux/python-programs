def largest_in_three(num1,num2, num3):
    if num1 > num2 :
        print("NUM! is big")
    elif num2 > num3:
        print("Num2 is big")
    elif num3 > num1:
        print("Num3 is big")
    elif num1 == num2 == num3:
        print("Equal")
    else:
        print("Nothing")

number1 = int(input("Enter Number 1 : "))
number2 = int(input("Enter Number 2 : "))
number3 = int(input("Enter Number 3 : "))


largest_in_three(number1, number2, number3)