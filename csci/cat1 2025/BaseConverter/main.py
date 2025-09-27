"""
BaseConverter.py

Converts data from one base to another base.

Converts from initial data with any base to base 10, before converting back to whatever the final conversion was supposed to be.

Base number indicates highest value (hex -> 16)

"""

## MODULES
import sys

## FUNCTIONS
def restartMain():
    # prompt the user to restart the program (called after every base conversion is fully complete)
    res = input("\033[33m> Restart the program? (y/n): ")

    if not res.lower().__contains__("y"):
        print("\033[31mExiting...")
        sys.exit()
    else:
        for i in range(1, 21):
            print("")
        main()


# valid bases, for printing out and so that the program knows the base.
validBases = {
    1: "Unary",
    2: "Binary",
    3: "Ternary",
    4: "Quaternary",
    5: "Quinary",
    6: "Senary",
    7: "Septenary",
    8: "Octal",
    9: "Nonary",
    10: "Decimal",
    11: "Undecimal",
    12: "Duodecimal",
    13: "Tridecimal",
    14: "Tetradecimal",
    15: "Pentadecimal",
    16: "Hexadecimal"
}

def keyPrint():
    # print out the different bases which the user can convert to

    print("\033[0m")
    print("** ENTER BASE NUMBER **")
    for i in validBases:
        print(f'\033[0m{i}. \033[34m{validBases[i]}') # print the different bases in order, cleaner than writing each base manually
    print("\033[0m")

def convertBase(value, initBase, convBase):
    # convert value between bases
    if initBase == 1:  # Unary
        decValue = len(value) # Unary is just the amount of ones
    else:
        decValue = baseToDecimal(str(value), initBase) # convert the value from any base to decimal

    # Convert decimal to base
    if convBase == 1:  # Unary
        return '1' * decValue

    if convBase == 10: # Decimal already calculated, so this is the value
        return str(decValue)

    # General base conversion for base 2+ (excl 10)
    digits = ("0"
              "1"
              "2"
              "3"
              "4"
              "5"
              "6"
              "7"
              "8"
              "9"
              "A"
              "B"
              "C"
              "D"
              "E"
              "F"
              "G"
              "H"
              "I"
              "J"
              "K"
              "L"
              "M"
              "N"
              "O"
              "P"
              "Q"
              "R"
              "S"
              "T"
              "U"
              "V"
              "W"
              "X"
              "Y"
              "Z")

    result = ""
    while decValue > 0:
        result = digits[decValue % convBase] + result
        decValue //= convBase

    return result if result else "0"


def baseToDecimal(value, initBase):
    # convert input to a decimal value

    value_str = str(value) # convert to string
    decValue = 0
    power = 0
    numValue = 0

    # Iterate through the string (reversed, because easier to know length and stuff)
    for digit in reversed(value_str):
        if '0' <= digit <= '9':
            numValue = ord(digit) - ord('0')  # string -> number, ord is the unicode symbol/character/number
        elif 'A' <= digit.upper() <= 'Z':  # hex
            numValue = ord(digit.upper()) - ord('A') + 10  # Convert A-Z -> 10-35

        # Ensure the digit is within the valid range (because the base number indicates the highest supported value for input)
        if numValue >= initBase:
            print(f"\033[31mInvalid digit '{digit}' for base {initBase}\033[0m")
            return ""

        # Compute the decimal value
        decValue += numValue * (initBase ** power)
        power += 1  # Increase power of base

    return decValue



def convertValue():
    # ask for the original base
    # ask for the value
    # ask for what to convert it to

    # get the original base for the user to convert to something else.
    keyPrint()

    baseInitInput = input("> Enter Base Number: ")

    global baseValueNum # global so no initialising number, and can be accessed from anywhere in the function
    global baseConvNum

    for i in range(1, 17):
        if baseInitInput.startswith(str(i)):
            baseValueNum = i

    # Get the value which the user wants to convert to another base
    convertValInput = input("> Enter Conversion Value: ")

    # Get the base to convert the value to
    baseConvInput = input("> Enter Base To Convert To: ")

    for i in range(1, 17):
        if baseConvInput.startswith(str(i)):
            baseConvNum = i


    initBase = ""
    convBase = ""

    for i in validBases:
        if baseValueNum == i:
            initBase = validBases[i]

        if baseConvNum == i:
            convBase = validBases[i]

    print(f'\033[035mConverting "{convertValInput}" from {initBase} to {convBase}...\033[0m')

    # Convert the bases based on input
    try:
        print(convertBase(str(convertValInput), int(baseValueNum), int(baseConvNum)))
    except:
        print("\033[31mInvalid input\033[0m")


## MAIN
def main():
    convertValue() # convert values
    restartMain() # restart the app if the user wants to


## RUN MAIN
main()
