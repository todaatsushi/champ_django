from workouts.helpers.helper import filterExercises, assignReps, changeTally


def makeCalisthenicsRoutine(data, target, reps):
    """
    Requires data to be appropriately filtered.

    Returns routine format dict of calisthenics weight exercises, according to
    specsand also appropriate rep lengths.
    """
    routine = {}

    # Get 5 calisthenics workouts
    # Pool together all exercises & sample
    pool = filterExercises(data, ["exercise_type", "muscle_group"],
                           [["Calisthenics", "Plyo"], [target.capitalize()]])

    # Get exercises
    exercises = pool.sample(5).exercise.tolist()

    for e in exercises:

        # Get exercise row in pool
        en = pool[pool.exercise.isin([e])]

        # Conditions for assigning reps
        valid = ["Plyo" in en.exercise_type.iloc[0],
                 "Cardio" in en.exercise_type.iloc[0],
                 "Hold" in en.movement_type.iloc[0]]

        # Check conditions
        if any(valid):
            # Assign plyo
            routine[e] = "15 seconds"

        else:
            # Assign calisthenics
            routine[e] = reps[0]

    return routine


def makeFullBodyRoutine(data, reps):
    """
    Requires data to be appropriately filtered.

    Returns routine format dict of full body / main lift weight exercises,
    according to specsand also appropriate rep lengths.
    """
    routine = {}

    # Pool together all relevant exercises & sample
    fullData = filterExercises(data, ["muscle_group"], [["Full"]])
    mainData = filterExercises(data, ["main_lift"], [["Yes"]])

    pool = fullData.append(mainData, ignore_index=True)

    # Sample the exercises
    exercises = pool.sample(6).exercise.tolist()

    # Loop through samples
    for e in exercises:

        # Get exercise row in pool
        en = pool[pool.exercise.isin([e])]

        # If weight in exercise, assign reps, else set time
        if "Weight" in en.exercise_type.tolist()[0]:

            routine[e] = reps[0]

        else:

            routine[e] = "15 seconds"

    return routine


def makeWeightRoutine(data, target, reps, parts):
    """
    Requires data to be appropriately filtered.

    Returns routine format dict of full body / main lift weight exercises,
    according to specsand also appropriate rep lengths.
    """
    routine = {}

    # Get exercises for target group & remove warmup exercises
    data = filterExercises(data, ["muscle_group"], [[target.capitalize()]])

    # Depending on target, initialise different tally totals
    if target in ["chest", "arms", "core"]:
        tot = 2
    else:
        tot = 1

    # Initialise tallies for parts in target group
    majorTally = {part: tot for part in parts}
    minorTally = {part: tot for part in parts}

    # Ensure inclusion of main compound lift

    # Get main exercise
    main = filterExercises(data, ["main_lift"], [["Yes"]])

    # Attribute main to tallies
    for index, exercise in main.iterrows():

        # Attribute exercises to tallies
        majorTally = changeTally(majorTally,
                                 [exercise.major_muscles[0]])

        minorTally = changeTally(minorTally,
                                 [exercise.minor_muscles[0]])

        # Add main exercise to the routine
        routine[exercise.exercise] = reps[0]

    # Get major exercises and chalk off as many minor counts as well
    for part in parts:

        # Get exercise entry from data
        exerciseEntry = filterExercises(data, ["major_muscles"],
                                        [[part]]).sample(1)

        # Assign appropriate reps to each exercise
        exReps = assignReps(exerciseEntry, reps)
        routine[exReps[0]] = exReps[1]

        # Update major & minor tallies
        majorTally = changeTally(majorTally,
                                 exerciseEntry.major_muscles.iloc[0])

        minorTally = changeTally(minorTally,
                                 exerciseEntry.minor_muscles.iloc[0])

    return routine
