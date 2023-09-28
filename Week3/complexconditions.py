# Write a program to determine whether to loan money based on the following rules.

# First, ask for a rating from 1–10 on the following:
print('For each of the following questions, please enter a rating from 1-10: ')

# How large is the loan?
loan = int(input('How large is the loan? '))

# How good is your credit history?
credit = int(input('How good is your credit history? '))

# How high is your income?
income = int(input('How high is your income? '))

# How large is your down payment?
down = int(input('How large is your down payment? '))

# Then, you will create a boolean variable for whether you should loan the money that will be set to either True or False. 
# Set up a series of if statements to decide if your decision to loan is "yes" or "no" according to the following rules:
should_loan = False # default value

# First, check if the loan size is at least 5. If it is, use the following rules:
if loan >= 5:
    # If the credit history and income are both at least 7, then the decision is "yes"
    if credit >= 7 and income >= 7:
        should_loan = True
    # If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"
    elif credit >= 7 or income >= 7:
        if down >= 5:
            should_loan = True
        else:
            should_loan = False
    # Otherwise (if neither the credit history nor income is at least 7), the decision is "no"
    else:
        should_loan = False

# Otherwise (if the loan is not 5 or greater), use these rules:
else:

    # If the credit is less than 4, then the decision is "no"
    if credit < 4:
        should_loan = False
    # Otherwise, check the following:
    else:
        # If either the income or the down payment is at least 7, the decision is "yes"
        if income >= 7 or down >= 7:
            should_loan = True
        # If both the income and the down payment are at least 4, then the answer is "yes"
        elif income >= 4 and down >= 4:
            should_loan = True
        # Otherwise, the decision is "no"
        else:
            should_loan = False

# Finally, display the decision to the user.
if should_loan:
    print('Yes, you should loan the money.')
else:
    print('No, you should not loan the money.')