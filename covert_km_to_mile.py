def km_to_mile(km):
    return km * 0.621

km = float(input("Enter Distance in Kilometer : "))

mile = km_to_mile(km)

print("Distance in Miles = ", mile)