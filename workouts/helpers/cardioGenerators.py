from workouts.helpers.helper import filterExercises
from random import randint


def makeHiitRoutine(data, reps):
    """
    Requires data to be appropriately filtered.

    Returns routine format dict of hiit cardio exercises, according to specs
    and also appropriate rep lengths.
    """

    # Initialise routine
    routine = {}

    # Filter data for hiit exercises
    data = filterExercises(data, ["exercise_type"], [["Plyo"]])

    # Take sample of 8 exercises
    hiitSample = data.sample(10).Exercise.tolist()

    # Insert rests
    hiitSample.insert(5, "Rest")
    hiitSample.insert(11, "Rest")

    # Loop through exercises and assign rep time
    for exercise in hiitSample:
        routine[exercise] = reps[0]

    # Return obj
    return routine


def makeRegularRoutine(data, reps, gearLevel):
    """
    Requires data to be appropriately filtered.

    Returns routine format dict of regular cardio exercises, according to specs
    and also appropriate rep lengths.
    """

    # Initialise routine
    routine = {}

    # Filter data for regular exercises
    data = filterExercises(data, ["exercise_type"], [["Cardio"]])

    # Due to lack of options, sample with replacement depending on avaliable
    # gear
    if gearLevel == "gymless":

        cardioSample = data.Exercise.sample(4, replace=True).tolist()

    else:

        cardioSample = data.Exercise.sample(4).tolist()

    # Loop through and assign rep length
    for exercise in cardioSample:

        routine[exercise] = reps[0]

    # Return obj
    return routine


def makeMixedRoutine(data, reps):
    """
    Requires data to be appropriately filtered.

    Returns routine format dict of both hiit & regular cardio exercises,
    according to specs and also appropriate rep lengths.
    """

    # Initialise tally & routine dicts
    routine = {}

    tally = {
        "Plyo": 4,
        "Cardio": 2
        }

    # Get exercises for both cardio types
    bothData = {
        "Plyo": filterExercises(data, ["exercise_type"], [["Plyo"]]),
        "Cardio": filterExercises(data, ["exercise_type"], [["Cardio"]])
        }

    # Loop through both types
    for cardioType in tally.keys():

        # Pool together possible exercises
        pool = bothData[cardioType].Exercise.tolist()

        # While tally is not 0 (not enough exercises)
        while tally[cardioType] > 0:

            # Get exercise
            exercise = pool.pop(randint(0, len(pool) - 1))

            # Add to routine
            routine[exercise] = reps[cardioType]

            # Adjust tally
            tally[cardioType] -= 1

    # Return obj
    return routine
