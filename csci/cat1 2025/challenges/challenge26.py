"""
Challenge 26

Code breaker

4 digit code
12 guesses
"""

## MODULE
import random

## FUNCTIONS
def generate():
    # make the code
    return [random.randint(0, 9) for _ in range(4)]

def feedback(code, guess):
    # let user know correct numbers
    correctpos = sum(c == g for c, g in zip(code, guess))

    # count digits in code and guess
    code_counts = {}
    guess_counts = {}
    for c, g in zip(code, guess):
        if c != g:
            code_counts[c] = code_counts.get(c, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    # correct, wrong position
    correctnonpos = sum(min(code_counts.get(d, 0), guess_counts.get(d, 0)) for d in guess_counts)

    return correctpos, correctnonpos


## MAIN
def main():
    code = generate()
    attempts = 12
    print("A 4 digit code got generated! Guess it!")

    # let user guess
    while attempts > 0:
        guess_input = input(f"Attempt {13 - attempts}/12: ")
        if len(guess_input) != 4 or not guess_input.isdigit():
            print("Please enter 4 digits.")
            continue

        guess = [int(d) for d in guess_input]

        # user feedback
        correct_pos, correct_wrong = feedback(code, guess)

        print(f"Correct digits in correct place: {correct_pos}")
        print(f"Correct digits in wrong place: {correct_wrong}")

        if correct_pos == 4:
            print("Congratulations! You've guessed the code.")
            break

        # attempts
        attempts -= 1

    else:
        # loser
        print(f"Sorry, you're out of attempts. The code was {''.join(map(str, code))}.")

while True:
    print("")
    main()
