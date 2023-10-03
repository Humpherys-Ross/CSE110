import random

# number = random.randint(1, 10)
# print(number)

keep_playing = "yes"

while keep_playing == "yes":
    magic_number = random.randint(1, 10)

    guess_count = 0

    guess = -1

    while guess != magic_number:
        guess = int(input("Guess a number between 1 and 10: "))
        guess_count += 1

        if guess < magic_number:
            print("Too low.")
        elif guess > magic_number:
            print("Too high.")
        else:
            print("You got it!")
            print(f"It took you {guess_count} guesses.")

    keep_playing = input("Do you want to play again (yes/no)? ")

print("Thanks for playing. Goodbye.")
