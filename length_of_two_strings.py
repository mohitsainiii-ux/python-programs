def maximum_length_string(a,b):
    if len(a) > len(b):
        return a
    elif len(b) > len(a):
        return b
    else:
        return "Both strings have equal length"

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

max_string = maximum_length_string(str1, str2)
print("The string with maximum length is:", max_string)