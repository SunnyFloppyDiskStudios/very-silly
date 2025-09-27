"""
main.py

*__Assessment Task: Dojo Student Query System__*

Allows a user to search through a database of dojo students.
Lets you filter and view information about them, such as: name, age, grade, belt, classes, fee
                                                           str  int   str    str    str    flt

Anything with startTime and executionTime() is purely to calculate how long program execution took.
It does not affect the other code

This code contains many different "protections", because users don't behave like we probably want them to, and they probably dont want to see raw errors
Protections include:
* prevent errors when user searching letter criteria in the number selection
* prevent errors when user putting words into numbers (like fee)
* prevent errors when user selects something out of the scope of the search (a user not listed)

Also, instead of printing dictionary values at the user, there's a function (prettyPrint) which lists it out nicely to read.
(it's named this way because some languages typically have a data.prettyPrint() for json (dictionaries))

From the main menu, the user is able to access a help article, which has simple instructions on how to use the program.
It also allows them to see how long program execution took if they would like to debug it, or for interest.

The easiest way to find the direct user is to type "1" and load student name.
It will immediately show their info if they are the only result in any search.
However, searching multiple criteria can be helpful to find users with low fees, or who take certain classes.

Searching by classes is inclusive, so if the student takes karate and judo, but user search for judo only, they will still show up.

This program has emphasis on user experience, so it is longer, however when you run the script you will find that it is very easy and intuitive.
"""

## MODULES
import os
import sys
import time
from decimal import Decimal as dec
import json

## JSON
with open("data.json", "r", encoding="utf-8-sig") as file: # encoding is required because file is formatted it differently
    members = json.loads(file.read()) # list of dictionaries containing student data


## FUNCTIONS
executeTimer = 0
def getCriteria(nums):
    # get the user's filter criteria into a dictionary to be iterated and checked against and find the students later
    crit = {}

    # get the criteria(s)
    if "7" in str(nums):
        # help "article"
        print("""
** HELP **

Using this script should be very simple.
To begin, you already got here by typing "7",
You can type in multiple numbers to filter a student from many criterias.
Try '23' to filter by age and belt as an example!
If multiple students are found, you will be prompted to select the one you want to find info about

When you select the student based on your filter criteria, the criteria will be highlighted.
This way, you will be able to easily pinpoint your criteria.
     
Potential Errors:
INVALID_AGE: You didn't enter a number or entered one with a decimal
INVALID_FEE: You didn't enter a number

>> Restart the program to continue
        """)
        sys.exit()
    if "8" in str(nums):
        global executeTimer # use it in function later
        executeTimer = True

    if "1" in str(nums):
        nameSearch = input("> Name: ")
        crit.update({"name": nameSearch}) # string

    if "2" in str(nums):
        try:
            ageSearch = int(input("> Age: "))
            crit.update({"age": ageSearch})  # int
        except:
            print("\033[31m>> Please enter a valid age. Error: INVALID_AGE")
            sys.exit()

    if "3" in str(nums):
        gradeSearch = input("> Grade: ")
        if "th" not in gradeSearch: # teenagers would be ideally 7-8th (maybe 4th) grade and above, therefore we need the "th" because the user might not put it there
            gradeSearch += "th"

        crit.update({"grade": gradeSearch}) # string

    if "4" in str(nums):
        beltSearch = input("> Belt Level: ")
        crit.update({"belt_level": beltSearch}) # string

    if "5" in str(nums):
        classSearch = input("> Classes (sep with comma): ")

        crit.update({"classes": [cls.strip() for cls in classSearch.split(",")]}) # list, strip removes spaces and split removes commas
    if "6" in str(nums):
        try:
            feeSearch = float(input("> Fee: "))
            crit.update({"fee": feeSearch})  # float
        except:
            print("\033[31m>> Please enter a valid fee. Error: INVALID_FEE.")
            sys.exit()
    return crit

def prettyPrint(sInfo):
    # print the result in a readable format, rather than raw dictionary
    # if in criteria, print as green, else white but still relevant so print anyways
    print()

    if "name" in criteria:
        print(f'    \033[32mName: {sInfo["name"]}\033[0m')
    else:
        print(f'    \033[0mName: {sInfo["name"]}\033[0m')

    if "age" in criteria:
        print(f'    \033[32mAge: {sInfo["age"]}\033[0m')
    else:
        print(f'    \033[0mAge: {sInfo["age"]}\033[0m')

    if "grade" in criteria:
        print(f'    \033[32mGrade: {sInfo["grade"]}\033[0m')
    else:
        print(f'    \033[0mGrade: {sInfo["grade"]}\033[0m')

    if "belt_level" in criteria:
        print(f'    \033[32mBelt Level: {sInfo["belt_level"]}\033[0m')
    else:
        print(f'    \033[0mBelt Level: {sInfo["belt_level"]}\033[0m')

    if "classes" in criteria:
        print(f"    \033[32mClasses: {', '.join(sInfo['classes'])}\033[0m")
    else:
        print(f"    \033[0mClasses: {', '.join(sInfo['classes'])}\033[0m")

    if "fee" in criteria:
        print(f'    \033[32mFee: ${sInfo["fee"]}\033[0m')
    else:
        print(f'    \033[0mFee: ${sInfo["fee"]}\033[0m')

    print()


def executionTime(start):
    # print execution time, but only if the execution filter flag was selected

    if executeTimer:
        print("\033[33mSearch time: ", dec(time.time()) - startTime)
        print("\033[0m")

    # "\033[__m" changes text colour
    # \033[31m --> red
    # \033[33m --> yellow


restart = False
def restartProgram():
    restartRequest = input("\033[35m> Enter anything to restart, or return 'exit' to quit: \033[0m")

    if restartRequest == "exit":
        sys.exit()
    else:
        print('\n'*80)
        main()


startTime = time.time()
criteria = {}
def main():
    ## INPUT
    # criteria numbers would make it easier to enter the result wanted by the user
    print("""
    ** FILTER KEY **
    
    1. name
    2. age
    3. grade
    4. belt_level
    5. classes
    6. fee
    \033[36m7. help
    \033[33m8. execution time
    """)

    print('\n'*10)

    criteriaNumbers = input("\033[0m> (num) enter filter numbers: ")
    if len(criteriaNumbers) == 0:
        print("\033[31m>> No filters selected!")
        restartProgram() # prevent the script from spitting out every single user in the database

    criteria = getCriteria(criteriaNumbers)

    ## CHECK STUDENTS AGAINST CRITERIAS
    startTime = dec(time.time())

    # checking classes seperately so that it can pick up students who slected multiple
    matchingStudents = []
    noClassCriteria = {key:value for key, value in criteria.items() if key != "classes"}  # Remove classes from criteria (strict check)
    for member in members:
        # check class criterias (inclusive)
        classMatch = False
        if "classes" in criteria:
            for cls in member["classes"]:
                if any(str(cls).lower() == str(critC).lower() for critC in criteria["classes"]): # lowercase so that input is always valid
                    classMatch = True
                    break  # prevent overwriting because classes stop matching
        else:
            classMatch = True  # No class criteria so all students pass

        # check rest of criterias (strict)
        criteriaMatch = all(str(noClassCriteria[key]).lower() == str(member[key]).lower() for key in noClassCriteria)
            # find student(s) which fit the criteria
            # all was used because it kept printing people not matching ALL criteria
            # converting to str(key).lower() makes it so that if the user types (example) "brown" instead of "Brown" it can still find the belt

        if classMatch and criteriaMatch: # if the student fits all the criteria
            if member["name"] not in matchingStudents: # no duplicaate
                matchingStudents.append(member["name"])

    ## GET MATCHING STUDENTS FROM CRITERIA
    if len(matchingStudents) == 0:
        print("\033[31m>> No students found!")
        executionTime(startTime)

        restartProgram()
    elif len(matchingStudents) == 1:
        # student was found from filter
        for member in members:
            if member["name"] == matchingStudents[0]:
                prettyPrint(member)
                executionTime(startTime)

                restartProgram()
    else:
        # multiple students under filter
        print("Qualifying Students:")
        for student in matchingStudents:
            print(student)

        selectedStudent = input("> Type the student you want to find (or 'all'): ")

        startTime = dec(time.time())

        if selectedStudent.lower() == "all":
            for match in matchingStudents:
                for member in members:
                    startTime = dec(time.time())
                    if member["name"] == match:
                        prettyPrint(member)
                        executionTime(startTime)

                        restartProgram()

        else:
            for member in members:
                if str(member["name"]).lower() == str(selectedStudent).lower():  # same reason as when initially searching students
                    prettyPrint(member)
                    executionTime(startTime)

                    restartProgram() # end of program because student is found

            print("\033[31m>> No matching student name") # end of program (if no result)

print('\n'*80) # clear anything and start at the bottom
main() # launch
