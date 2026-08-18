def count_frequency(text):
    count = {}

    for char in text:
        count[char] = count.get(char, 0) + 1

    for char, number in count.items():
        print(f"{char},{number}", end=" ")

text = input("Enter String : ")

count_frequency(text)