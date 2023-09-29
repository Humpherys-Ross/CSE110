# I have added a death and game over scenario to the game. There is one option in each branch that will lead to a game over.
# I have also added a restart function that will restart the game if the user makes an invalid choice or reaches a game over scenario.

# Create your own text-based adventure game with at least three levels of choices. 
# It's up to you to determine the scenarios, the choices, and the consequences.

# Keep in mind the following guidelines and requirements:

# You need to have at least three levels of scenarios with possible choices. (This means that every time the user 
# plays the game they should answer at least three questions because every branch of the game should go three levels deep.)

# Scenarios that follow an earlier answer should be handled with nested if statements. In other words, 
# the body/block of the first if statement will contain a print statement and then another if statement inside it.

# At least one of your scenarios must have more than two possible choices.

# In each prompt, write the choices in ALL CAPS, so that the user knows which words are possible responses to choose.

# When checking the users responses, you should match on the keyword, regardless of the uppercase/lowercase used in
# the response (e.g., "match", "MATCH", "Match" should all work).

# Making different choices should take you to different scenarios. (You shouldn't have the same result for different choices.)

# Choices should only work for the correct question.

# In other words, if one scenario resulted in choices of Run/Hide, but another resulted in choices Follow/Look, you should not be able to respond 
# with "Follow" to the question that asked for Run/Hide.

# A good way to accomplish this is to have a series of nested if statements. (That is, the print and then the next if statement will be within the body/block of the first if statement.)

# For each question, you should provide an "else" clause to handle the case that the user tries to type something other than the possible choices.
# It is up to you how to handle this case.

def main_game():
    # Starting point of the game.
    print("\nWelcome to the 'Escape from Draken Castle'!\n")
    print("You are imprisoned in the infamous Draken Castle. The only light filtering in is from the bars in a high window.")
    
    # Level 1 Choices
    print("\n1) What will you do?")
    print("- DIG beneath the floor using your spoon.")
    print("- WAIT for the guard to doze off.")
    print("- SING a haunting tune.")
    # get user input and convert to uppercase so we get a match regardless of case 
    response = input().upper()

    # Level 1 Branches
    if response == "DIG":
        dig_branch()
    elif response == "WAIT":
        wait_branch()
    elif response == "SING":
        sing_branch()
    else:
        # if the user enters an invalid choice, restart the game
        print("\nInvalid choice. Restarting the adventure.")
        # call the main_game function to restart the game
        main_game()

def dig_branch():
    # Branch for choosing to DIG.
    print("\nYou discover a hidden passage below!")
    
    # Level 2 Choices
    print("\n2) The passage splits into three:")
    print("- FOLLOW the left tunnel.")
    print("- GO straight down the middle.")
    print("- TAKE the right tunnel.")
    # get user input and convert to uppercase so we get a match regardless of case 
    response = input().upper()

    # Level 2 Branches
    if response == "FOLLOW":
        print("\nThe tunnel leads outside, but a pitfall catches you off-guard.")
        # call the game_over function to restart the game
        game_over()
    elif response == "GO":
        print("\nYou stumble upon an underground chamber filled with glowing gems.")
        
        # Level 3 Choices
        print("\n3) What do you do?")
        print("- TOUCH a gem.")
        print("- EXIT the chamber.")
        print("- HIDE and observe.")
        # get user input and convert to uppercase so we get a match regardless of case 
        response = input().upper()

        # Level 3 Branches
        if response == "TOUCH":
            print("\nThe gem emits a blinding light and you vanish. Game Over.")
            # call the game_over function to restart the game
            game_over()
        elif response == "EXIT":
            print("\nYou cautiously exit the chamber, making your way to freedom!")
        elif response == "HIDE":
            print("\nFrom your hiding spot, you observe a secret exit!")
        else:
            # if the user enters an invalid choice, restart the game
            print("\nInvalid choice. Restarting the adventure.")
            # call the main_game function to restart the game
            main_game()

    elif response == "TAKE":
        print("\nThe tunnel is filled with traps. You narrowly dodge them and find a way out!")
    else:
        # if the user enters an invalid choice, restart the game
        print("\nInvalid choice. Restarting the adventure.")
        # call the main_game function to restart the game
        main_game()

def wait_branch():
    # Branch for choosing to WAIT.
    print("\nThe guard eventually falls asleep.")
    
    # Level 2 Choices
    print("\n2) What's your next move?")
    print("- GRAB the keys silently.")
    print("- ATTACK the guard.")
    print("- SLIP past the guard.")
    # get user input and convert to uppercase so we get a match regardless of case
    response = input().upper()

    # Level 2 Branches
    if response == "GRAB":
        print("\nSuccess! You have the keys in hand.")
        
        # Level 3 Choices
        print("\n3) What's your next action?")
        print("- UNLOCK your cell.")
        print("- FREE other prisoners.")
        print("- THROW keys at the guard.")
        # get user input and convert to uppercase so we get a match regardless of case
        response = input().upper()

        # Level 3 Branches
        if response == "UNLOCK":
            print("\nYou successfully unlock your cell and escape the castle!")
        elif response == "FREE":
            print("\nThe prisoners rally together and overpower the guards. Freedom is yours!")
        elif response == "THROW":
            print("\nThe keys clang loudly, waking up the guard. Game Over.")
            # call the game_over function to restart the game
            game_over()
        else:
            # if the user enters an invalid choice, restart the game
            print("\nInvalid choice. Restarting the adventure.")
            # call the main_game function to restart the game
            main_game()

    elif response == "ATTACK":
        print("\nThe guard overpowers you. Game Over.")
        # call the game_over function to restart the game
        game_over()
    elif response == "SLIP":
        print("\nYou make your way silently, finding a map of the castle!")
    else:
        # if the user enters an invalid choice, restart the game
        print("\nInvalid choice. Restarting the adventure.")
        # call the main_game function to restart the game
        main_game()

def sing_branch():
    # Branch for choosing to SING.
    print("\nYour haunting melody attracts a curious maid.")
    
    # Level 2 Choices
    print("\n2) How do you respond to her approach?")
    print("- ASK her to help.")
    print("- BEFRIEND her.")
    print("- THREATEN her.")
    # get user input and convert to uppercase so we get a match regardless of case
    response = input().upper()

    # Level 2 Branches
    if response == "ASK":
        print("\nThe maid, moved by your plight, offers you a hidden escape route.")
        
        # Level 3 Choices
        print("\n3) How do you proceed?")
        print("- FOLLOW her instructions.")
        print("- DECEIVE and bind her.")
        print("- GIVE her a gift in gratitude.")
        # get user input and convert to uppercase so we get a match regardless of case
        response = input().upper()

        # Level 3 Branches
        if response == "FOLLOW":
            print("\nYou follow her instructions and successfully escape!")
        elif response == "DECEIVE":
            print("\nThe maid screams, alerting the guards. Game Over.")
            # call the game_over function to restart the game
            game_over()
        elif response == "GIVE":
            print("\nTouched by your kindness, she helps you find the safest way out.")
        else:
            # if the user enters an invalid choice, restart the game
            print("\nInvalid choice. Restarting the adventure.")
            # call the main_game function to restart the game
            main_game()

    elif response == "BEFRIEND":
        print("\nOver time, you earn her trust. She assists in your escape!")
    elif response == "THREATEN":
        print("\nStartled, the maid alerts the guards. Game Over.")
        # call the game_over function to restart the game
        game_over()
    else:
        # if the user enters an invalid choice, restart the game
        print("\nInvalid choice. Restarting the adventure.")
        # call the main_game function to restart the game
        main_game()

def game_over():
    # Handles the game over scenario and restarts the game.
    print("\nYou've met an unfortunate end. Restarting the adventure...")
    # call the main_game function to restart the game
    main_game()


# Start the game
if __name__ == "__main__": main_game()