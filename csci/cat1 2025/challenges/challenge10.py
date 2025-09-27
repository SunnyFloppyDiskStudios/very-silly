"""
Challenge10.py

Rock, Paper, Scissors!

"""

## MODULE
import random

## FUNCTION
def main():
    # input
    print("""
** MATERIALS **
    
1. ROCK -- r -- 1
2. PAPER -- p -- 2
3. SCISSORS -- s -- 3
    """)

    player = input("> Rock, Paper, Scissors: ")

    player = player[0] # first char

    if player[0].lower() == "r":
        player = 1
    elif player[0].lower() == "p":
        player = 2
    elif player[0].lower() == "s":
        player = 3
    else:
        print("Enter a Valid Choice!")
        return

    # computer
    computer = random.randint(1, 3)

    # win conditions
    if player == computer:
        print("Tie!")
        return
    elif player > computer:
        print("You Win! Computer Chose: " + str(computer))
        return
    elif player < computer:
        print("You Lose! Computer Chose: " + str(computer))
        return

## LOOP
while True:
    main()