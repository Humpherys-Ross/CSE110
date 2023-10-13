# I added the ability to add quantities for the items in the card as well as
# the ability to remove a certain quantity of an item from the cart. If the
# quantity of an item is 1, it will just remove it. Otherwise, it will ask
# the user how many of the item they would like to remove.

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
quantity = []


# def add item and ask for price
def add_item():
    # ask user for item and capitalize the item
    item = input("What item would you like to add? ").capitalize()
    # ask user for price
    price = float(input(f"What is the price of '{item}'? "))
    # ask user for quantity
    item_quantity = int(input(f"How many '{item}' would you like to add? "))
    # add item to cart
    cart.append(item)
    # test to view item added to the array
    # print(cart)
    # add price to prices
    prices.append(price)
    # test to view price added to the array
    # print(prices)
    # print item added to cart
    # add quantity to quantity
    quantity.append(item_quantity)
    # test to view quantity added to the array
    # print(quantity)
    print(f"{item_quantity} of '{item}' has been added to the cart.")
    print()


# def view cart including prices
def view_cart():
    # if cart is empty, print cart is empty
    if not cart:
        print("The cart is empty.")
    # else print items in cart
    else:
        print("The contents of the shopping cart are:")
        # for each item in cart, print item and price
        # using the enumerate function to get the index of the item
        for index, item in enumerate(cart):
            # print item and price in the following format:
            # 1. Item - $price x quantity
            print(f"{index + 1}. {item} - ${prices[cart.index(item)]:.2f} x "
                  f"{quantity[cart.index(item)]}")
    print()


# def remove item
def remove_item():
    # if cart is empty, print cart is empty
    if not cart:
        print("The cart is empty.")
    # else print items in cart
    else:
        # ask user for item number to remove from cart
        item_num = int(input("Which item would you like to remove? "))
        # find index of item in cart and remove item
        if 0 < item_num <= len(cart):
            if quantity[item_num - 1] > 1:
                remove_quantity = int(input(f"How many of "
                                            f"'{cart[item_num - 1]}' would you"
                                            f" like to remove? "))
                if remove_quantity < quantity[item_num - 1]:
                    quantity[item_num - 1] -= remove_quantity
                    print(f"{remove_quantity} of '{cart[item_num - 1]}' has "
                          f"been removed from the cart.")
                elif remove_quantity == quantity[item_num - 1]:
                    # use the pop method to remove the item from the list
                    cart.pop(item_num - 1)
                    # use the pop method to remove the price from the list
                    prices.pop(item_num - 1)
                    # use the pop method to remove the quantity from the list
                    quantity.pop(item_num - 1)
                else:
                    print("Invalid quantity. No items removed.")
            else:
                # use the pop method to remove the item from the list
                cart.pop(item_num - 1)
                # use the pop method to remove the price from the list
                prices.pop(item_num - 1)
                # use the pop method to remove the quantity from the list
                quantity.pop(item_num - 1)
                print("Item removed.")
        # else print item not in cart
        else:
            print("Sorry, we couldn't find that item in the cart.")
    print()


# def compute total
def compute_total():
    # print total price of cart and format to 2 decimal places
    total_price = sum(price * quantity for price, quantity in zip(prices,
                                                                  quantity))
    print(f"The total price of the cart is ${total_price:.2f}\n")


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
