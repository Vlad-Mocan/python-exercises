import numbers

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def is_even(num):
    return num % 2 == 0


def maximum_number(num1, num2):
    if num1 >= num2:
        return num1
    return num2


def count_vowels(word):
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


def sum_of_numbers(items):
    sum_numbers = 0
    for item in items:
        if isinstance(item, (int, float)):
            sum_numbers += item
        # if isinstance(item, numbers.Number):
        #     sum_numbers += item
    return sum_numbers


def is_in_list(items, number):
    return number in items and isinstance(number, numbers.Number)


print(is_even(5))
print(maximum_number(3, 4))
print(count_vowels("test"))
print(sum_of_numbers([1, 2, 3, 4]))
print(is_in_list([1, 2, "test"], 2))
