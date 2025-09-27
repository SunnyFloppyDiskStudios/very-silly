"""
Challenge 1

Joke (very funny)
"""

beginning = "Why did the chicken cross the road?"
punchline = "To get to the other side (hahaha)"

# print the joke (awaiting input)s
go = input(beginning)

if len(go) > -1:
    print("\033[35m" + punchline)