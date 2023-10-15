# Open the HR System file for reading
with open("Week6/hr_system.txt", "r") as file:
    # Read through the file line by line
    for line in file:
        # Remove leading and trailing whitespace and split the line into parts
        parts = line.strip().split(" ")

        # Check if there are at least 2 parts (name and title)
        if len(parts) >= 4:
            name = parts[0]  # First part is the name
            id_number = parts[1]  # Second part is the ID number
            title = parts[2]  # Third part is the title
            salary = float(parts[-1])  # Last part is the salary

            paycheck = salary / 24.0

            if "Engineer" in title:
                paycheck += 1000.0

            # Display the name and title
            print(f"{name} (ID: {id_number}), {title} - ${paycheck:.2f}")
