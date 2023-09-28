# Write a program that asks the user for two integers then, write three
# different if statements as follows:

print('What is the first number? ')
first = int(input())

print('What is the second number? ')
second = int(input())

# If the first integer is greater than the second, print "The first integer is greater"
# Otherwise, print "The first number is not greater"

if first > second:
    print('The first integer is greater')
else:
    print('The first number is not greater')

# If the two numbers are equal, print "The numbers are equal". Otherwise, print "The numbers are not equal"

if first == second:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

# If the second number is greater than the first, print "The second integer is greater". Otherwise, print "The second number is not greater"

if second > first:
    print('The second integer is greater')
else:
    print('The second number is not greater')

print() # blank line

# Have a program ask the user for their favorite animal. Then write an if statement as follows:

print('What is your favorite animal? ')
animal = input()

# Check to see if the user's favorite animal is the same as your favorite animal (meaning you, the programmer).
# If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite." 
# Verify that it works regardless of the capitalization.

if animal.lower() == 'dog':
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')

