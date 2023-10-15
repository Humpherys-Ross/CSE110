with open("hr_system.txt", "r") as hr_file:
    for line in hr_file:
        parts = line.split(",")

    if len(parts) >= 2:
        name = parts[0]
        title = ",".join(parts[1:])

    print(f"Name: {name}, Title: {title}.")
