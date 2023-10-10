# For this project you will create a program that stores a list of products in
# a shopping cart along with their prices. The user should have the ability to
# add items to the list, remove them, and see the total price of the cart.

# For the milestone deliverable, you only need to worry about storing a list of
# the names of the items (not the prices yet), and only need to be able to add
# new items and display the list. Then, for the complete project, you'll add
# the ability to store the prices, remove items, and compute the total.

# Assignment
# For this project, the user will be given a menu and have the ability to
# choose items from the menu. The options in the menu include the following:

# 1 Add a new item
# 2 Display the contents of the shopping cart
# 3 Remove an item (only needed for the final project deliverable)
# 4 Compute the total (only needed for the final project deliverable)
# 5 Quit

# When the user chooses one of these options, the program should perform the
# appropriate action. Then the program should show them the menu again, and
# allow them to choose another option. It should continue running until the
# user choose the option to quit.

# Milestone:
# By the middle of the week, to help make sure you are on track to finish the
# assignment, you need to complete the following:

# 1 Have menu system that repeats until the user chooses quit.
# 2 Create a list that will store the names of the items in the shopping cart.
# 3 Complete the option to add the name of the item to the list.
# 4 Complete the option to display the names of the items in the list.

print("Welcome to the Shopping Cart Program!")
# create empty list
cart = []
prices = []


# def add item and ask for price
def add_item():
    # ask user for item and capitalize the item
    item = input("What item would you like to add? ").capitalize()
    # ask user for price
    price = float(input(f"What is the price of '{item}'? "))
    # add item to cart
    cart.append(item)
    prices.append(price)
    # print item added to cart
    print(f"'{item}' has been added to the cart.")
    print()


# def view cart
def view_cart():
    # print contents of cart
    print("\nThe contents of the shopping cart are: ")
    # loop through cart and print each item
    for item in cart:
        print(item)
    print()


# def remove item
def remove_item():
    # ask user for item and capitalize the item
    item = input("What item would you like to remove? ").capitalize()
    # remove item from cart
    cart.remove(item)
    # print item removed from cart
    print(f"'{item}' has been removed from the cart.")
    print()


# def compute total
def compute_total():
    # print total price of cart and format to 2 decimal places
    print(f"The total price of the cart is ${sum(prices):.2f}")
    print()


# def quit
def quit():
    # print goodbye message
    print("Thank you for using the Shopping Cart Program. Goodbye!")
    # exit program
    exit()


def show_menu():
    # print menu
    while True:
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View Cart")
        print("3. Remove item")
        print("4. Compute the total")
        print("5. Quit")
        # ask user for choice
        choice = int(input("\nPlease enter an option: "))
        print()

        # if choice == 1, call add item
        if choice == 1:
            add_item()
        # if choice == 2, call view cart
        elif choice == 2:
            view_cart()
        # if choice == 3, call remove item
        elif choice == 3:
            remove_item()
        # if choice == 4, call compute total
        elif choice == 4:
            compute_total()
        # elif choice == 5, call quit
        elif choice == 5:
            quit()
        # else print invalid choice
        else:
            print("Invalid choice. Please try again.")
            # call show menu
            show_menu()


# Start the program
if __name__ == "__main__":
    show_menu()
