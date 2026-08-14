sentence = input("Enter a sentence: ")
upperletters = 0
lowerletters = 0

for char in sentence:
    if char.isupper():
        upperletters += 1
    elif char.islower():
        lowerletters += 1
print("UPPER CASE LETTERS", upperletters)
print("LOWER CASE LETTERS", lowerletters)