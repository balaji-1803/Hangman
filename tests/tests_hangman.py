import os
import sys

# Add src to path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_PATH = os.path.join(PROJECT_ROOT, "src")
sys.path.insert(0, SRC_PATH)

from hangman.hangman import loadWords, chooseWord, isWordGuessed, getGuessedWord


def test_load_words():
    words = loadWords()
    assert isinstance(words, list)
    assert len(words) > 0


def test_choose_word():
    words = loadWords()
    word = chooseWord(words)
    assert word in words


def test_guess_helpers():
    secret = "abc"
    assert not isWordGuessed(secret, ["a"])
    assert isWordGuessed(secret, ["a", "b", "c"])
    assert getGuessedWord(secret, ["a"]) == "a_ _ "
