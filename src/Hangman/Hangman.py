import os
import random
import string

BASE_DIR = os.path.dirname(__file__)
WORDLIST_FILENAME = os.path.join(BASE_DIR, "words.txt")


def loadWords():
    """Load words from text file."""
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, "r", encoding="utf-8") as f:
        words = f.read().split()
    print(f"  {len(words)} words loaded.")
    return words


def chooseWord(wordlist):
    """Return a random word."""
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    """Check if all letters of secretWord are guessed."""
    return all(letter in lettersGuessed for letter in secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    """Show guessed characters and underscores."""
    return "".join(ch if ch in lettersGuessed else "_ " for ch in secretWord)


def getAvailableLetters(lettersGuessed):
    """Return remaining letters."""
    all_letters = list(string.ascii_lowercase)
    for g in lettersGuessed:
        if g in all_letters:
            all_letters.remove(g)
    return "".join(all_letters)


def hangman(secretWord, max_guesses=8):
    """Start an interactive Hangman game."""
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")

    lettersGuessed = []
    mistakesMade = 0

    while mistakesMade < max_guesses:
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            return True

        print("-------------")
        print("You have", max_guesses - mistakesMade, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").strip().lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Enter one lowercase letter.")
            continue

        if guess in lettersGuessed:
            print("Oops! You already guessed that letter:",
                  getGuessedWord(secretWord, lettersGuessed))
            continue

        lettersGuessed.append(guess)

        if guess in secretWord:
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
            mistakesMade += 1
            print("Oops! That letter is not in my word:",
                  getGuessedWord(secretWord, lettersGuessed))

    print("-------------")
    print("Sorry, you ran out of guesses. The word was", secretWord)
    return False


if __name__ == "__main__":
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)