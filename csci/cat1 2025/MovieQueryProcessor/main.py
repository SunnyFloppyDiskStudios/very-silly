"""
MovieQueryProcessor.py
Sorts out a database of movies, orders it how the user wants it to be, and then lets the user search through these movies.

first ask for sorting criteria as well as ascending or descending
sort the data by this criteria

then, ask the user what to search for
and print out the results which match, in the sorted order


sorting:

selected 1,2,3
2 sorted within 1, 3 sorted within 2, nested sorting (sorts within sorts)


-- EXAMPLE OF HOW TO DO SORTING --
criteria = ["year", "genre", "title"]
             ^ primary

year      genre         title

1900         comedy -   ac
                    -   bc
                    -   cc
        documentary -   ad
                    -   bd
             horror -   ah
                    -   bh

1920         comedy -   ac2
                    -   ba2
        documentary -   ad2
                    -   bd2
             horror -   ah2
                    -   bh2
"""

## MODULES
import sys
import time
import json

## JSON
with open("data.json", "r", encoding="utf-8-sig") as file: # encoding is required because format
    movies = json.loads(file.read())

## FUNCTIONS
sortCriteria = []
def getSortCriteria():
    # get the criteria of stuff which should be sorted in, based on selection (i.e. sort by title and year)

    validVals = {
        "1":"title",
        "2":"year",
        "3":"genre",
        "4":"rating",
        "5":"director",
        "6":"duration",
        "a":"ascending",
        "d":"descending",
        "h":"help",
        "q":"quit",
        "p":"printAll"
    }

    print("""
** SORTING CRITERIA KEYS **
1. title
2. year
3. genre
4. rating
5. director
6. duration

p. print ALL sorted output

a. Ascending (default)
d. Descending

h. help
q. quit
    """)

    sortCritInp = input("> Enter criteria numbers (in order of sort): ")

    for i in sortCritInp:
        if i in validVals and not i in sortCriteria:
            sortCriteria.append(validVals[i])


searchCriteria = {}
def getSearchCritiera():
    # get the criteria of specific things to search for. printed out in the order of the above sort.
    # does not print everything just because in sort. seperate option for user.

    validVals = {
        "1": "title",
        "2": "year",
        "3": "genre",
        "4": "rating",
        "5": "director",
        "6": "duration",
    }

    print("""
    
** SEARCHING CRITERIA KEYS **
1. title
2. year
3. genre
4. rating
5. director
6. duration

q. quit
        """)

    searchCritInp = input("> Enter criteria numbers: ")

    for i in searchCritInp:
        if i in validVals and not i in searchCriteria:
            v = input(f'> {validVals[i]}: ')
            searchCriteria[validVals[i]] = v

        if i.startswith("q"):
            print("\033[31mStopped program")
            sys.exit()


def prettyPrint(data):
    # neatly print data for reading
    for d in data:
        print(f"""
\033[0mTitle: \033[36m{d["title"]}
\033[0mYear: \033[36m{d["year"]}
\033[0mGenre: \033[36m{d["genre"]}
\033[0mRating: \033[36m{d["rating"]}/10
\033[0mDirector: \033[36m{d["director"]}
\033[0mDuration: \033[36m{d["duration"]} minutes

""")


sortedData = []
def quickSort(arr, keys, descending):
    # quick sort, to sort database
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2] # center of arrray
    left = [x for x in arr if compare(x, pivot, keys, descending) < 0]
    middle = [x for x in arr if compare(x, pivot, keys, descending) == 0]
    right = [x for x in arr if compare(x, pivot, keys, descending) > 0]

    return quickSort(left, keys, descending) + middle + quickSort(right, keys, descending)

def compare(a, b, keys, descending): # ^ quick sort, finding the greater/less than values
    for key in keys:
        if a[key] < b[key]:
            return -1 if not descending else 1
        elif a[key] > b[key]:
            return 1 if not descending else -1
    return 0


def sortData(order): # (call) function which handles sorting, and calls quickSort
    descending = "descending" in order # check if the order has "descending", then set it true if it does
    sort_keys = [key for key in sortCriteria if key in ["title", "year", "genre", "rating", "director", "duration"]]
    sortedData = quickSort(movies, sort_keys, descending)

    for c in sortCriteria:
        if c == "quit":
            print("\033[31mStopped program")
            sys.exit()

        if c == "help":
                print("""
** HELP ARTICLE **
Welcome to the help section.
This program was designed to be easy to use,
simply enter the numbers of the criteria for sorting/searching, like 13 to set criteria by title and genre.
Entering special letter characters often have a special result, which are outlined on the keys  list.
        
\033[35m RESTART THE PROGRAM TO CONTINUE
                    """)
                sys.exit()

    for c in sortCriteria:
        if c == "printAll":
            print(sortedData)

movieResults = []
def searchData(crit):
    # search for movies based on critieria
    results = []

    for m in movies:
        results = {key:value for key, value in crit.items()}
        criteriaMatch = all(str(results[key]).lower() == str(m[key]).lower() for key in results)

        if criteriaMatch:
            movieResults.append(m)

    prettyPrint(movieResults)

def restartMain(): # restarts the program if the user wants to
    resInput = input("\033[35mRestart? (y/n): \033[0m")
    resInput = resInput.lower()

    if resInput.startswith("y"):
        main()
    else:
        sys.exit()

## MAIN
startTime = time.time()
criteria = {}

def main():
    # set blank to prevent repetitions among repeats
    criteria.clear()
    sortCriteria.clear()
    movieResults.clear()
    searchCriteria.clear()
    sortCriteria.clear()
    sortedData.clear()

    # program
    getSortCriteria() # ask user for sorting criteria
    sortData(sortCriteria) # sort out the data, printing it all out if the user asked for it in the input
    getSearchCritiera() # ask user for movies to search for
    searchData(searchCriteria)# print out the movies that they searched for
    restartMain()

## RUN PROGRAM
main()
