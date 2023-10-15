with open("Week6/books.txt", "r") as file:
    for line in file:
        clean_line = line.strip()
        print(clean_line)
