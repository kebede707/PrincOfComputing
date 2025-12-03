# Function Code
def checkGuess(guess, secret_word):
    feedback = []  # store '+', '~', 'x'
    
    # Loop through each position i in the guess
    for i in range(len(secret_word)):
        letter_found = False

        # First check: correct position
        if guess[i] == secret_word[i]:
            feedback.append('+')
            letter_found = True

        else:
            # Second check: letter exists somewhere else in the secret word
            for j in range(len(secret_word)):
                if guess[i] == secret_word[j]:
                    feedback.append('~')
                    letter_found = True
                    break  # stop checking other positions

        # Third check: letter was not found at all
        if not letter_found:
            feedback.append('x')

    return feedback
