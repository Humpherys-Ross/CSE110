# added an array for words to be picked at random and I added a limited number of guesses. It shows the correct answer if you run out of guesses

import random
# By the middle of the week, to help make sure you are on track to finish the assignment, you need to complete the following:

# Have a secret word stored in the program.

# Prompt the user for a guess.

# Continue looping as long as that guess is not correct.

# Calculate the number of guesses and display it at the end.

# You do not need to have any hints at this point.

# print("Welcome to the Word Guessing Game!")

# secret_word = "mosiah"
# guess_count = 0
# answer = ""

# while secret_word != answer:
#     answer = input("Guess a word: ")
#     if secret_word != answer:
#         print("Incorrect. Try again.")
#         guess_count += 1
#     else:
#         print("Correct!")
#         guess_count += 1
#         print(f"It took you {guess_count} guesses.")

# In addition to the Milestone requirements, your final program must:

# 1 Use a loop to generate the initial hint.

# 2 Add a check to verify that the length of the guess is the same as the length of the secret word. If it is not, display a message. If they are the same, then proceed to give the hint.

# 3 Add the hints according to the rules above.

# 4 Make sure to account for the following in your hints:

#   Letters that are not present at all in the secret word (underscore _).

#   Letters that are present in the secret word, but in a different spot (lowercase).

#   Letters that are present in the secret word at that exact spot spot (uppercase).
def wordpuzzle():
    print("Welcome to the Word Guessing Game!")
    print("You have 10 guessesto find the correct word.")

    # Initialize guess count
    guess_count = 0 
    # Initialize total guesses
    total_guesses = 10
    # Initialize answer 
    answer = "" 

    # Make array of words
    word_array = ["Apple","Brave","Chair","Drive","Earth","Flare","Ghost","Heart","Inlet","Juice"]
    # Choose random word from array 
    secret_word = random.choice(word_array).lower() 
    # verify that the secret word is chosen correctly
    # print(secret_word) 

    #check the length of the secret word
    secret_word_length = len(secret_word)
    # verify that the length of the secret word is correct
    # print(secret_word_length) 

    # Generate initial hint
    hint = "_" * secret_word_length

    # Prompt the user for a guess
    while secret_word != answer and guess_count < total_guesses:
        # Display hint
        print(f"\nThe hint is: {hint}") 
        # Prompt user for guess
        answer = input("Guess a word: ").lower() 
        # Check if the length of the guess is the same as the length of the secret word
        if len(answer) != secret_word_length:
            # Increment guess count
            guess_count += 1 
            print(f"Sorry, the guess must have the same number of letters as the secret word. You have {total_guesses - guess_count} guesses remaining.")
            # If the guess has the same length, display wrong letters as "_", letters in the wrong spot as lowercase, and letters in the right spot as uppercase
        elif secret_word != answer:
            for i in range(secret_word_length):
                # Verify that the letters are being compared correctly
                # print(f"Comparing {answer[i]} with {secret_word[i]}")
                if answer[i] == secret_word[i]:
                    # Display letters in the right spot as uppercase
                    hint = hint[:i] + answer[i].upper() + hint[i + 1:] 
                elif answer[i] in secret_word:
                    # Display letters in the wrong spot as lowercase
                    hint = hint[:i] + answer[i].lower() + hint[i + 1:] 
                else:
                    # Display letters that are not present as "_"
                    hint = hint[:i] + "_" + hint[i + 1:]
            # Increment guess count 
            guess_count += 1 
            print(f"Incorrect. You have {total_guesses - guess_count} guesses remaining.")
        # If the guess is correct, display congratulations and the number of guesses
        else:
            print("\nCongratulations! You guessed the secret word!")
            # Increment guess count
            guess_count += 1 
            print(f"It took you {guess_count} guesses.")
            # Exit the loop since the guess is correct
            break
    # If the guess is incorrect and the guess count is equal to the total guesses, display that the user ran out of guesses and the secret word
    if secret_word != answer:
        print(f"\nSorry, you ran out of guesses. The secret word was {secret_word}.")

# start the game
wordpuzzle()