import random

from word import words
import string


def get_valid_word(words):
    """Returns a valid word from the list of words that matches the given word length."""
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)  # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what user has guessed
    while len(word_letters) > 0:
        print("You have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print(
                f"You have already guessed the letter {user_letter}. Try another one!"
            )
        else:
            print(f"Invalid letter. Please try again.")
    print(f"\n🎉 Congratulations! You guessed the word: {word}")

hangman()
