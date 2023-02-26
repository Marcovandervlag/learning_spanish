import random
import urllib.request
import json
# This function reads a list of words from a URL and filters them by category
def load_words(category):
    # Open the URL and read its contents as a string
    with urllib.request.urlopen('https://raw.githubusercontent.com/Marcovandervlag/learning_spanish/main/spanish_words.json') as f:
        content = f.read().decode('utf-8')    
    # Parse the string as a JSON object
    words = json.loads(content)
    # If a category was specified, filter the words to only include those in that category
    if category:
        words = [(w['english'], w['spanish'], w['category']) for w in words if w['category'] == category]
    else:
        words = [(w['english'], w['spanish'], w['category']) for w in words]    
    # Return the filtered words
    return words
# This function prompts the user to select a category and returns their choice
def get_category():
    # Define a dictionary mapping menu options to category names
    options = {
        '1': 'Korfball',
        '2': 'Food',
        '3': 'Drink',
        '4': 'Hobbies',
        '5': 'Greetings',
        '6': 'Looks',
        '7': 'Colors',
        '8': 'Weather',
        '9': 'Objects',
        '10': 'Days',
        '11': 'Months',
        '12': 'vervoeging',
        '13': 'numbers',
        '14': 'onetoten'        
    }
    # Loop until the user selects a valid option
    while True:
        print("Select a category:")
        # Print the menu options
        for key, value in options.items():
            print(f"{key}. {value}")
        # Read the user's choice from the keyboard
        print("type random if you want to randomize it")
        choice = input()
        if choice == "random":
            break
            
        # If the choice is valid, return the corresponding category name
        elif choice in options:
            return options[choice]
        # Otherwise, print an error message and loop again
        print("Invalid choice, please try again.")
# This function selects a random word from a list of words
def get_word(words):
    return random.choice(words)
# This function prompts the user to translate a word and returns True if the translation is correct, False otherwise
def translate(word):
    english_word, spanish_word, category = word
    guess = input(f"What is the Spanish word for {english_word}? ")
    return guess.lower() == spanish_word.lower()
# This function plays the game, prompting the user to translate 10 random words from the specified category
def play_game(category=None):
    # Load the words for the specified category (or all categories if none is specified)
    total_words = int(input("How many words do you want?\n:"))
    words = load_words(category)
    # Initialize counters for the number of correct and total answers
    correct = 0
    total = 0
    # Loop until 10 words have been translated
    while total < total_words:
        # Select a random word from the list
        word = get_word(words)
        # Prompt the user to translate the word
        if translate(word):
            # If the translation is correct, increment the correct counter and print a success message
            print("Correct!")
            correct += 1
        else:
            # Otherwise, print the correct translation
            print(f"Incorrect. The correct answer is {word[1]}")
        # Increment the total counter
        total += 1
    # Print the final score
    print(f"Game over! You scored {correct} out of {total}.")
    category = get_category()
    play_game(category)
# This is the main entry point for the program
if __name__ == '__main__':
    category = get_category()
    play_game(category)
    # Prompt the user to play
