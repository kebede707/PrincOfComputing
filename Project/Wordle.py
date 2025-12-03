# Main Program

from wordList import wordList
from checkGuess import checkGuess
import random

secret_word = random.choice(wordList)
attempts_made = 0

print(secret_word) # to be removed

difficulty_level = ["easy", "medium", "hard"]
attempts_limit = [10, 6, 4]

while True:
    selection = input("Select difficulty (easy, medium, or hard): ")

    if selection in difficulty_level:
        index = difficulty_level.index(selection)
        max_attempts = attempts_limit[index]
        break
    else:
        print("Please enter valid level exactly as prompted.")

print(f"You selected {selection}. You have {max_attempts} attempts to guess the word.")
print("After each guess you will get a series of symbols to indicate if you are correct.")
print("+ meens the letter is in the correct spot. ~ means it is in the wrong spot. X means it is not in the word.")

while attempts_made < max_attempts:
    # validate guess
    while True:
        guess = input("Input your guess: ").lower()
        if guess in wordList:
            break
        print("Invalid word. Please enter a valid word from the word list.")

    
    attempts_made += 1

    result = checkGuess(guess, secret_word)

    if guess == secret_word:
        print("You Won!!!")
        break

    print(result)
    print(f"Attempts left: {max_attempts - attempts_made}")

else:
    # runs only if loop ends WITHOUT break
    print("You lost. The correct word was:", secret_word)
