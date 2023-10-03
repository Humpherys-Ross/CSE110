# Write a program that asks the user for their favorite letter. Then, loop
# through a programmed word one letter at a time. If the letter in the
# programmed word is the user's favorite, you'll first print it out as a
# capital letter, then later you will "hide" it. If the letter is not their
# favorite you will print it out as a lower case letter.

word = 'commitment'

favorite_letter = input('What is your favorite letter? ')

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print('_', end='')
    else:
        print(letter.lower(), end='')
print()
