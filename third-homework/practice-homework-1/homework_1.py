vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def analyze_word(word):
    if not isinstance(word, str):
        return

    number_of_vowels = 0
    for letter in word:
        if letter in vowels:
            number_of_vowels += 1
    return {"Length": len(word), "Vowels": number_of_vowels, "Uppercase": word.upper()}


print(analyze_word("python"))
