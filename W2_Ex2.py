def count_words(text):
    text = text.lower()
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

text = input("Enter a text: ")
print(count_words(text))