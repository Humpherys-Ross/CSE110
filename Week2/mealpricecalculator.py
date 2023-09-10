# Ask the user for the following:

# - The price of a child's meal (floating point)
# - The price of an adult's meal (floating point)
# - The number of children (integer)
# - The number of adults (integer)

# - Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by the price of their meal, 
#   and multiplying the number of adults by the price of their meal and adding those two values together.
# - Display the subtotal.
# - Ask the user for the sales tax rate as a percentage (floating point). Please note that this percentage should 
#   be entered and stored as a number such as 6, or 6.5, not 0.06 or 0.065.
# - Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.
# - Compute and display the total price of the meal by adding the subtotal and the sales tax.

# Finally:

# - Ask the user for the the payment amount (floating point)
# - Compute and display the change.

# ---------------------------------------------------------------------------------------------

# Mid week requirements for Meal Price Calculator

# By midweek, to help make sure you are on track to finish the assignment, you need to complete the following:

# - Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.
# - Ask the user for the number of adults and children and store these values properly into variables as integers.
# - Compute and display the subtotal (you do not need to worry about the sales tax or rounding to two decimals at this point).

# ---------------------------------------------------------------------------------------------

# Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.
child_meal = float(input('What is the price of a child meal? '))
adult_meal = float(input('What is the price of an adult meal? '))

# Ask the user for the number of adults and children and store these values properly into variables as integers.
num_children = int(input('How many children are there? '))
num_adults = int(input('How many adults are there? '))

# Compute and display the subtotal, no need to include sales tax or rounding.
subtotal = (child_meal * num_children) + (adult_meal * num_adults)

# Display the subtotal.
print(f'The subtotal is ${subtotal:.2f}')

# ---------------------------------------------------------------------------------------------