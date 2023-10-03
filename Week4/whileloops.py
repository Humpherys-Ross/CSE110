# Write a Python Program that does each of the following:

# Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number.

number = int(input("Enter a positive number: "))

while number < 0:
    print("That number is negative. Please enter a positive number.")
    number = int(input("Enter a positive number: "))

print(f"The number is {number}.")

# Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you."

answer = ''

while answer != 'yes':
    answer = input("Can I have a piece of candy? ")

print("Thank you.")