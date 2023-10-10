# Ask the user for a list of list of items in a shopping list, stop asking for
# items when the user types "quit."

# Then complete the following:

# Loop through the items in the regular way (for example, for thing in
# the_list) and display each one to make sure you have the initial list built
# correctly.

# Add another loop to go through and print the items in the list, but this
# time, instead of using the for ... in syntax, use an index (for example,
# for ... in range) and then access the item using the index and the square
# brackets. Print the index in front of the items like so: 0. Milk

# Ask the user for an index and a new shopping list item. Replace the item at
# that index with the new item. Then, display the whole list again.

print("Enter a list of items in your shopping list, type 'quit' to stop.")

the_list = []

item = input("Enter an item: ")

while item != "quit":
    the_list.append(item)
    item = input("Enter an item: ")

print("\nThe shopping list:")
for item in the_list:
    print(item)

print("\nThe shopping list with indexes:")
for i in range(len(the_list)):
    item = the_list[i]
    print(f"{i}. {item}")

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

the_list[index] = new_item

print("\nHere is your new list:")
for i in range(len(the_list)):
    item = the_list[i]
    print(f"{i}. {item}")
