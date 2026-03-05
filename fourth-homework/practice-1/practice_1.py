def copy_file(source: str, destination: str):
    with open(source, "r", encoding="utf-8") as file1:
        with open(destination, "w", encoding="utf-8") as file2:
            content = file1.read()
            file2.write(content)


copy_file("source.txt", "./copy.txt")
copy_file("source.txt", "./destination-test/copy.txt")
