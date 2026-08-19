def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius = float(input("Enter Temprature in celsius : "))

fahrenheit = celsius_to_fahrenheit(celsius)

print("Temprature in Fahrenheit : ", fahrenheit)