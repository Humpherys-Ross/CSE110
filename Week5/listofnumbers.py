# Work through these core requirements step-by-step to complete the program.
# Please don't skip ahead and do the whole thing at once, because others on
# your team may benefit from building the program up slowly.

# Compute the sum, or total, of the numbers in the list.

# Compute the average of the numbers in the list.

# Find the maximum, or largest, number in the list.

print("Enter a list of numbers (you may include negative numbers), type '0' to"
      " stop.")

numbers = []

# Continue to ask a user for a number until they enter 0.
while True:
    # Ask the user for a number.
    number = int(input("Enter a number: "))
    # If the number is 0, stop asking for numbers.
    if number == 0:
        break
    # Otherwise, add the number to the list.
    numbers.append(number)

# Compute the total of the numbers in the list.
# We use the sum function to add up all the numbers in the list.
total = sum(numbers)

# Compute the average of the numbers in the list.
# We need to find the length of the list, so we use len(numbers).
average = total / len(numbers)

# Find the maximum number in the list.
# We use the max function to find the maximum number in the list.
maximum = max(numbers)

# print the total, average, and maximum.
print(f"\nThe total is {total}")
print(f"The average is {average}")
print(f"The maximum is {maximum}")

# Stretch goals:

# Have the user enter both positive and negative numbers, then find the
# smallest positive number (the positive number that is closest to zero).

# Sort the numbers in the list and display the new, sorted list.

# Find the smallest number in the list.
# We use the min function to find the smallest number in the list.
smallest = min([num for num in numbers if num > 0])

# Sort the numbers in the list.
# We use the sorted function to sort the numbers in the list.
sorted_numbers = sorted(numbers)

# Print the smallest number and the sorted list.
print(f"The smallest positive number is {smallest}")
print("The sorted list is:")
for number in sorted_numbers:
    print(number)
