"""
Challenge 3

Rectangular Prism/Cuboid Size Calculator
"""

## MODULE
from decimal import Decimal as dec

## FUNCTIONS
def is_number(value):
    # conversion ability
    try:
        dec(value)
        return True
    except:
        return False

def main():
    # inputs
    le = input("\n> Length: ")
    wi = input("> Width: ")
    he = input("> Height: ")

    if not is_number(le) or not is_number(wi) or not is_number(he):
        print("Please enter valid numbers!")
        return

    # calculations
    size = dec(le) * dec(wi) * dec(he)

    print(str(size) + " square units ")

## LOOP
while True:
    main()