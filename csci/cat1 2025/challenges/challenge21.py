"""
Challenge21.py

put names into an array, and then print out all the names, as well as finding duplicates.
"""

## VARIABLE
names = [] # names added

## FUNCTION
while True:
    name = input("Enter name: ")
    if name.lower() == "exit" or name.lower() == "quit" or name == "":
        break # exit loop
    names.append(name.lower())

# array holding the name counts
name_counts = {}
for name in names:
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

# duplicates
print("\nDuplicates:")
duplicates_found = False
for name, count in name_counts.items():
    if count > 1:
        print(f"{name.capitalize()} is a duplicate ({count} times).")
        duplicates_found = True

if not duplicates_found:
    print("No duplicates found.")

# print all the names
print("\nUsers: ")
unique_names = set(names)
for name in sorted(unique_names):
    print(name.capitalize())