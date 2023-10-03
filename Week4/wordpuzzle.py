# By the middle of the week, to help make sure you are on track to finish the assignment, you need to complete the following:

# Have a secret word stored in the program.

# Prompt the user for a guess.

# Continue looping as long as that guess is not correct.

# Calculate the number of guesses and display it at the end.

# You do not need to have any hints at this point.

print("Welcome to the Word Guessing Game!")

secret_word = "mosiah"
guess_count = 0
answer = ""

while secret_word != answer:
    answer = input("Guess a word: ")
    if secret_word != answer:
        print("Incorrect. Try again.")
        guess_count += 1
    else:
        print("Correct!")
        guess_count += 1
        print(f"It took you {guess_count} guesses.")