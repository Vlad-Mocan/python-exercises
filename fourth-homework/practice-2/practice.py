from string import punctuation


def count_words_from_file(filename: str) -> int:
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            for char in punctuation:
                line = line.replace(char, "")
            count += len(line.split())

    return count


print(count_words_from_file("story.txt"))
