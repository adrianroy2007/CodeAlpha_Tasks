import random

# List of 5 predefined words
words = ["python", "computer", "school", "program", "keyboard"]

# Select a random word
word = random.choice(words)

# Variables for the game
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Main game loop
while incorrect_guesses < max_incorrect_guesses:
    # Display the current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_incorrect_guesses - incorrect_guesses)

    # Check if the player has guessed the complete word
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Check whether the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the letter to the guessed letters
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Incorrect guess!")

# If the player uses all 6 incorrect guesses
if incorrect_guesses == max_incorrect_guesses:
    print("\nGame Over!")
    print("The word was:", word)