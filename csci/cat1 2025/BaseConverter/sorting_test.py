# """
# sorting_test.py
# just a file for testing out the conversion function
#
# https://byjus.com/gate/conversion-of-bases-to-other-bases-notes/ (non-python, explanation on how to convert bases)
#
# ** COMPATIBILITIES **
# (c) characters, (i) int, (s) string
# INPUT -> user input
# OUTPUT -> converted
# (in) supports val input
# (co) supports val conversion output
#
# 1 INPUT 1-FF, outputs "1" as many times as decimal len (max int 10 chars) (only 0 to unary is incompatible) (converting large values to unary is a VERY BAD idea)
# 2 INPUT value must ONLY contain 0s and/or 1s (if value is being converted FROM base 2)
# 3 i (co),((input) highest number is 2), allows INPUT string, OUTPUT num, only if INPUT BASE is 11+
# 4 i (co) ((input) highest number is 3), >^
# 5 i (co) ((input) highest number is 4), >^
# 6 i (co) ((input) highest number is 5), >^
# 7 i (co) ((input) highest number is 6), >^
# 8 i (co) ((input) highest number is 7), >^
# 9 i (co) ((input) highest number is 8), >^
# 10 i (co)((input) highest number is 9), >^
# 11 si (in/co) ((input) highest letter is "A")
# 12 si (in/co) ((input) highest letter is "B")
# 13 si (in/co) ((input) highest letter is "C")
# 14 si (in/co) ((input) highest letter is "D")
# 15 si (in/co) ((input) highest letter is "E")
# 16 si (in/co) ((input) highest letter is "F") (16 to 1, 0-F)
# """
#
# def convertBase(value, initBase, convBase):
#     # Convert input to a decimal value
#     if initBase == 1:  # Unary
#         decValue = len(value) # Unary is just the amount of ones
#     else:
#         decValue = baseToDecimal(str(value), initBase) # convert the value from any base to decimal
#
#     # Convert decimal to base
#     if convBase == 1:  # Unary
#         return '1' * decValue
#
#     if convBase == 10: # Decimal already calculated, so this is the value
#         return str(decValue)
#
#     # General base conversion for base 2+ (excl 10)
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     result = ""
#     while decValue > 0:
#         result = digits[decValue % convBase] + result
#         decValue //= convBase
#
#     return result if result else "0"
#
#
# def baseToDecimal(value, initBase):
#     value_str = str(value) # convert to string
#     decValue = 0
#     power = 0
#     numValue = 0
#
#     # Iterate through the string (reversed, because easier to know length and stuff)
#     for digit in reversed(value_str):
#         if '0' <= digit <= '9':
#             numValue = ord(digit) - ord('0')  # string -> number, ord is the unicode symbol/character/number
#         elif 'A' <= digit.upper() <= 'Z':  # hex
#             numValue = ord(digit.upper()) - ord('A') + 10  # Convert A-Z -> 10-35
#
#         # Ensure the digit is within the valid range (because the base number indicates the highest supported value for input)
#         if numValue >= initBase:
#             raise ValueError(f"Invalid digit '{digit}' for base {initBase}")
#
#         # Compute the decimal value
#         decValue += numValue * (initBase ** power)
#         power += 1  # Increase power of base
#
#     return decValue
#
#
# ## TEST
# def testConversion(t):
#     print("TESTS:")
#
#     for i in range(1, 17): # initial base
#         for j in range(1, 17): # convert base
#             try:
#                 cb = convertBase(t, i, j)
#
#                 if cb == "":
#                     print(f'\033[33merror at i{i} and j{j}\033[0m')
#                 else:
#                     print(f'i{i}, j{j} -- {cb}')
#
#             except:
#                 print(f'\033[33merror at i{i} and j{j}\033[0m')
#
#
# testConversion("1D") # testing value
#
