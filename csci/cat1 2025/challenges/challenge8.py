"""
Challenge 8

Legal to vote?
"""

while True:
    age = input("\nHow old? ")

    if age.isnumeric():
        if int(age) > 18:
            print("You can vote!")

        else:
            print("You cannot vote!")
    else:
        print("Hey.. that's not an age!")