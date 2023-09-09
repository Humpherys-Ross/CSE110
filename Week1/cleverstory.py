# Madlib story where user inputs words to fill in the blanks
# I added a function to determine "a" or "an" based on the first letter of the word
# I added a .upper() method to the exclamation1 variable to make it all uppercase
# I also added two more sentences at the end of the original story with some nouns and an additional adjective

# Get user input
adjective1 = input("Enter an adjective: ")
animal1 = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
exclamation1 = input("Enter an exclamation: ")
verb2 = input("Enter a verb: ")
verb3 = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
noun2 = input("Enter a noun: ")
noun3 = input("Enter a noun: ")

# Function to determine "a" or "an" based on first letter of word
def a_or_an(word):
    if word[0].lower() in 'aeiou':
        return 'an'
    else:
        return 'a'
    
# "The other day, I was really in trouble. It all started when I saw {a_or_an(adjective1)} {adjective1} {animal1} {verb1} down the hallway.\n
# \"{exclamation1.upper()}!\" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop,\n
# but not before it tried to {verb3} right in front of my {noun1}. It was my {adjective2} {noun2}!\n
# I couldn't believe my eyes. My {noun3} just stood there in shock."


# Set story to a string
story = f"The other day, I was really in trouble. It all started when I saw {a_or_an(adjective1)} {adjective1} {animal1} {verb1} down the hallway.\n\"{exclamation1.upper()}!\" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop,\nbut not before it tried to {verb3} right in front of my {noun1}. It was my {adjective2} {noun2}!\nI couldn't believe my eyes. My {noun3} just stood there in shock."

# Print the story
print('Your story is:')
print(story)