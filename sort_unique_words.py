def sort_unique_words(text):
    words = text.split()
    words = set(words)
    words = sorted(words)
    return words

text = input("Enter words: ")
result = sort_unique_words(text)
print(result)