# Main Program

from wordList import wordList
import random

secret_word = random.choice(wordList)
attempts_made = 0

print(secret_word)

difficulty_level = ["easy", "medium", "hard"]
attempts_limit = [10, 6, 4]

selection = input("Select difficulty (easy, medium, or hard): ")