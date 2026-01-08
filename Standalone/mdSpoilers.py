# adds markdown spoilers to EVERY character in a message.

thing = input("thing: ")
things = []

for i in thing:
    things.append("||" + i + "||")

print("".join(things))
