import pandas as pd
from django_pandas.io import read_frame

from workouts.models import Exercise


def check(list1, list2):
    """
    Checks if any value in list1 exists in list2
    """
    for i in list1:
        for n in list2:
            if i == n:
                return True
    return False


def isinList(data, col, filterAll):
    """
    Takes input data and returns a list of bool values, where all rows
    where any variable in filterAll appears in col (of data) is True for
    that index, else is False.
    """
    boolList = []

    # Iterate through all lists in col,
    for i in range(data[col].size):
        # Temporary value of list in Series
        entry = data[col].iloc[i]

        # Ensure proper usage (needs a list to check properly)
        if isinstance(entry, list) is False:
            entry = [entry]

        # Do elements in filterAll appear in entry
        inFilterAll = check(entry, filterAll)
        # Indicate for that index if we want it
        boolList.append(inFilterAll)

    # Return boolList of desired rows
    return boolList


def exerciseData():
    """
    Get exercise data and format it for python, returning it for use
    """

    exercises = Exercise.objects.all()
    data = read_frame(exercises)

    # Create columns of lists from cols with multiple answers
    for i in range(3, 11):
        data.iloc[:, i] = data.iloc[:, i].apply(lambda x: str(x))
        data.iloc[:, i] = data.iloc[:, i].apply(lambda x: x.split(","))

    return data


def filterExercises(data, cols, filterList):
    """
    Applies isinList to data across all cols with index aligned filters.
    data must be a dataframe, cols a list of strings with column names &
    filterList a list of lists with all row options to extract.

    Col names and the desired filter options must be index aligned!
    Returns data, filtered and index reset.
    """

    # Loop through the columns and filter throught with associated indicies
    for n in range(len(cols)):
        # Filter down
        data = data[isinList(data, cols[n], filterList[n]
                             )].reset_index(drop=True)

    return data


def changeTally(tallyDict, keysList):
    """
    Takes a tally in form of a dictionary. Iterates over all
    elements in keyList and for those that exist in the dict,
    """
    for i in keysList:
        if i in list(tallyDict.keys()):
            tallyDict[i] -= 1

    return tallyDict


def assignReps(exercise, allReps):
    """
    Takes a dataframe entry as an input as well as all available
    reps defined by user. Assigns exercise to appropriate rep value.
    Returns a dict with key of exercise name and value of one set's
    work. Assumes that allReps (if relevant) is in ascending order.

    Assigns larger sets for traditionally lighter, isolated
    exercises
    """

    # Extract data from exercise
    name = exercise.exercise.iloc[0]
    exType = exercise.exercise_type.iloc[0][0]
    mvmt = exercise.movement_type.iloc[0][0]
    cOrI = exercise.compound_isolation.iloc[0][0]
    sl = exercise.sl.iloc[0][0]

    # Check if hold
    if mvmt == "Hold":
        ret = [name, "30 seconds"]
        # Return object
        return ret

    # Check allRange length
    if len(allReps) == 3:
        # Check conditions for higher reps
        if exType == "Calisthenics" or cOrI == "Isolation":
            ret = [name, allReps[2]]
        elif cOrI == "Compound" and sl == 'Yes':
            ret = [name, allReps[0]]
        elif cOrI == "Compound":
            ret = [name, allReps[1]]
        else:
            raise ValueError("Couldn't sort exercise")
    else:
        ret = [name, allReps[0]]
    print(ret)
    return ret
