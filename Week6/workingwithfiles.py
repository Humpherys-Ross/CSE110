with open('books.txt', 'r') as file:
    for line in file:
        clean_line = line.strip()
        print(clean_line)