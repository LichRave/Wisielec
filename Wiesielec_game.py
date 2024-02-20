import random
from typing import List

words = ["jazz", "warcaby", "krokodyl", "statek", "samochod", "samolot", "pociag"]
word = random.choice(words)
guessed_word = ["_" for char in word]
lifes = 5


def draw_word_letters(word: List[str]):
    print("".join(word))


def check_letter_in_word(word: str, letter: str, guessed_word: List[str]) -> bool:
    result = False
    if letter in word:
        for index, char in enumerate(word):
            if char == letter:
                guessed_word[index] = letter
                result = True
    return result


def is_win(guessed_word: List[str]) -> bool:
    return all([char != "_" for char in guessed_word])


def user_input(guessed_word: List[str]) -> str:
    selected_letter = input("Zgadnij litere: ")
    #letter_in_guess = [char == selected_letter for char in guessed_word]
    while selected_letter in guessed_word:
        print("Litera już została odgadnięta.")
        selected_letter = input("Zgadnij litere: ")
        # letter_in_guess = [char == selected_letter for char in guessed_word]
    return selected_letter


draw_word_letters(guessed_word)
while True:
    selected_letter = user_input(guessed_word)
    if not check_letter_in_word(word, selected_letter, guessed_word):
        lifes -= 1
        print(f"Pozostało {lifes} prób")
    draw_word_letters(guessed_word)
    if lifes <= 0:
        print("Przegrałeś! HAHA")
        break
    if is_win(guessed_word):
        print("Wygrałeś!!!! Brawo.")
        break