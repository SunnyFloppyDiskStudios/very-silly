"""
Challenge 12

Factor Finder
"""

from decimal import Decimal as dec

def isNum(value):
    # conversion ability
    try:
        dec(value)
        return True
    except:
        return False

def getFactors(n):
    # get the num factors
    n = int(n)
    return [i for i in range(1, n + 1) if n % i == 0]

## LOOP
while True:
    number = input("\n> Number: ")

    # input
    if isNum(number):
        num = dec(number)
        if num != int(num) or num < 2:
            print("Please enter a whole number greater than 1.")
            continue

        factors = getFactors(num)
        if len(factors) == 2:
            print(f"Prime Number!")
        else:
            print(f"Factors: {factors}")
    else:
        print("Enter a number!")
