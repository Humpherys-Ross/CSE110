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
    print("\nWelcome to the 'Escape from Draken Castle'!\n")
    print("You are imprisoned in the infamous Draken Castle. The only light filtering in is from the bars in a high window. As you contemplate your fate, three choices present themselves:")
    
    print("\n1) What will you do?")
    print("- DIG beneath the floor using your spoon.")
    print("- WAIT for the guard to doze off and try to steal his keys.")
    print("- SING a haunting tune to lure someone closer.")
    
    response = input().upper()

    if response == "DIG":
        print("\nHours seem like days, but your determination pays off. You discover a hidden passage below!")
        print("\n2) The passage splits into three:")
        print("- FOLLOW the left tunnel.")
        print("- GO straight down the middle.")
        print("- TAKE the right tunnel.")
        
        response = input().upper()
        
        if response == "FOLLOW":
            print("\nThe tunnel leads to the outside, but you are immediately spotted by the guards. They end your escape attempt permanently.")
            main_game()
        elif response == "GO":
            print("\nWalking cautiously, you suddenly step into a room filled with treasure and a hidden exit!")
        elif response == "TAKE":
            print("\nYou find yourself in the castle's dungeons. However, an unnoticed open cell leads to a secret exit!")
        else:
            print("\nInvalid choice. Restarting the adventure.")
            main_game()
    
    elif response == "WAIT":
        print("\nAfter what seems like eternity, the guard starts snoring loudly.")
        print("\n2) What's your next move?")
        print("- GRAB the keys silently.")
        print("- ATTACK the guard with your chains.")
        print("- SLIP past the guard without confronting him.")
        
        response = input().upper()

        if response == "GRAB":
            print("\nSuccess! You unlock your cell and find an unguarded exit!")
        elif response == "ATTACK":
            print("\nAs you try to overpower the guard, he awakens and calls for backup. They swiftly end your escape and your life.")
            main_game()
        elif response == "SLIP":
            print("\nYou quietly move past the guard and find yourself in a long corridor leading to freedom!")
        else:
            print("\nInvalid choice. Restarting the adventure.")
            main_game()

    elif response == "SING":
        print("\nYour haunting melody attracts a curious maid.")
        print("\n2) How do you respond to her approach?")
        print("- ASK her to help you escape.")
        print("- BEFRIEND her and gain her trust.")
        print("- THREATEN her to open the cell.")
        
        response = input().upper()

        if response == "ASK":
            print("\nThe maid, feeling pity, gives you a map and a key. Following her instructions, you find a secret exit!")
        elif response == "BEFRIEND":
            print("\nYou and the maid become friends. She discreetly helps you escape during her next visit!")
        elif response == "THREATEN":
            print("\nStartled, the maid screams, attracting the guards who ensure you never threaten anyone again.")
            main_game()
        else:
            print("\nInvalid choice. Restarting the adventure.")
            main_game()
    
    else:
        print("\nInvalid choice. Restarting the adventure.")
        main_game()

# Start the game!
main_game()
