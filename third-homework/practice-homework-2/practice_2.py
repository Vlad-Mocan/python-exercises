def delete_duplicates(items):
    return list(set(items))


def max_age(items):
    if len(items) == 0:
        return

    max_value = items[0][1]
    for item in items:
        if item[1] > max_value:
            max_value = item[1]
    return max_value


def most_frequent(numbers):
    if not numbers:
        return None

    seen_numbers = {}
    for number in numbers:
        if number in seen_numbers:
            seen_numbers[number] += 1
        else:
            seen_numbers[number] = 1

        # seen_numbers[number] = seen_numbers.get(number, 0) + 1

    max_value = -1
    most_frequent_number = None

    for key, value in seen_numbers.items():
        if value > max_value:
            max_value = value
            most_frequent_number = key

    return most_frequent_number


def most_frequent_word(text):
    word_list = text.lower().split()
    if not word_list:
        return None

    seen_words = {}
    for word in word_list:
        seen_words[word] = seen_words.get(word, 0) + 1

    max_value = 0
    most_freq_word = None

    for key, value in seen_words.items():
        if value > max_value:
            max_value = value
            most_freq_word = key

    return most_freq_word


def change_dictionary(name_age_dictionary):
    new_dict = {}
    for key, value in name_age_dictionary.items():
        new_dict[value] = key
    return new_dict


print(delete_duplicates([1, 1, 1, 1, 1, 1, 12, 3, 4, 24, 2, 32]))
print(max_age([("test", 23), ("john", 60), ("mike", 30)]))
print(most_frequent((1, 2, 1, 1, 1, 2, 3, 4, 2, 3)))
print(most_frequent_word("apple banana apple orange banana apple"))
print(change_dictionary({"test": 23, "john": 60, "mike": 30}))
