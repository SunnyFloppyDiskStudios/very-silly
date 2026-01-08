# removes spoilers from every single character that is inputted. The reverse of the mdSpoilers.py script.

thing = input("thing: ")
things = []

for i in thing:
    if i != "|":
        things.append(i)

print("".join(things))
