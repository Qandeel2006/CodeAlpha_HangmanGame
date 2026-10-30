# Task 1: Hangman Game
import random

words = ["python", "apple", "chair", "house", "music"]
word = random.choice(words)   # pick a random word

# The drawing of the man for 0, 1, 2, ... 6 wrong guesses
stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========="""
]

guessed = []       # letters the player has guessed
wrong = 0          # number of wrong guesses
max_wrong = 6

print("Welcome to Hangman!")
print("You can make", max_wrong, "wrong guesses.")
print(stages[wrong])

while wrong < max_wrong:
    # show the word with _ for letters not guessed yet
    display = ""
    for letter in word:
        if letter in guessed:
            display = display + letter + " "
        else:
            display = display + "_ "
    print("\nWord:", display)

    # check if the player won
    if "_" not in display:
        print("You won! The man is saved!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please type only one letter.")
    elif guess in guessed:
        print("You already guessed that letter.")
    else:
        guessed.append(guess)
        if guess in word:
            print("Correct!")
        else:
            wrong = wrong + 1
            print("Wrong! You have", max_wrong - wrong, "guesses left.")
            print(stages[wrong])   # draw one more part of the man

if wrong == max_wrong:
    print("\nGame over! The man was hanged.")
    print("The word was:", word)