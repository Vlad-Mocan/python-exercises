def number_stats(numbers):
    if len(numbers) == 0:
        return "No numbers given"

    number_of_odd_numbers = 0

    for number in numbers:
        if number % 2 != 0:
            number_of_odd_numbers += 1

    return (
        min(numbers),
        max(numbers),
        sum(numbers) / len(numbers),
        number_of_odd_numbers,
    )


print(number_stats([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# def number_stats(numbers):
#     if len(numbers) == 0:
#         return "No numbers given"

#     number_of_odd_numbers = 0
#     sum_numbers = 0
#     max_number = numbers[0]
#     min_number = numbers[0]

#     for number in numbers:
#         sum_numbers += number

#         if number % 2 != 0:
#             number_of_odd_numbers += 1

#         if number > max_number:
#             max_number = number
#         if number < min_number:
#             min_number = number

#     return (
#         min_number,
#         max_number,
#         sum_numbers / len(numbers),
#         number_of_odd_numbers,
#     )
