# Main Program

import wordList.py
import random

secret_word = random.choice(wordList)
attempts_made = 0

difficulty_level = ["easy", "medium", "hard"]
attempts_limit = [10, 6, 4]

selection = input("Select difficulty (easy, medium, or hard): ")