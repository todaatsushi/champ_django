import pandas as pd
from workouts.helpers.helper import filterExercises
from workouts.helpers.cardioGenerators import makeHiitRoutine, \
    makeRegularRoutine, makeMixedRoutine
from workouts.helpers.weightGenerators import makeCalisthenicsRoutine, \
    makeFullBodyRoutine, makeWeightRoutine


class Workout(object):
    """
    Workout class objects are objects with all necessary inputs from
    the user to make a full workoutself.

    generate(Warmup/Routine) are used to make content as they start empty.
    formatFullRoutine is used to assign reps and sets.
    """

    def __init__(self, data, target, allParts, repRanges, gear):
        """
        Input data: pandas DataFrameself.
        target - string: if a cardio workout - has to be workout type. Else,
        a target muscle group - has to be in data.
        allParts: list of strings - containing all sub muscle groups. If
        cardio, should be a None type.
        repRanges: list - of rep ranges in ascending order.
        gear: string - Level of gym equipment available.
        """
        super().__init__()

        self.data = data
        self.target = target
        self.parts = allParts
        self.rr = repRanges
        self.warmup = {}
        self.routine = {}
        self.gear = gear

    def __str__(self):
        return f'{target.capitalize()} Workout'

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def setTarget(self, newTarget):
        self.target = newTarget

    def getTarget(self):
        return self.target

    def setParts(self, newParts):
        self.parts = newParts

    def getParts(self):
        return self.parts

    def setRepRanges(self, newRepRanges):
        self.rr = newRepRanges

    def getRepRanges(self):
        return self.rr

    def getWarmup(self):
        return self.warmup

    def setWarmup(self, newWarmup):
        self.warmup = newWarmup

    def setRoutine(self, newRoutine):
        self.routine = newRoutine

    def getRoutine(self):
        return self.routine

    def getGear(self):
        return self.gear

    def generateWarmup(self):
        """
        Uses class properties to output a workout warmup. Returns a dict,
        of key:value pairs where key is an warmup exercise with a value of
        of one set's worth of work
        """
        genData = self.getData()

        # Get muscle group exercises
        warmupData = filterExercises(genData, ["exercise_type"],
                                     [["Calisthenics", "Plyo"]])

        # Possible rep ranges for warmups
        warmupRR = ["5 seconds", "10 seconds", "15 seconds"]

        # Full body exercises
        fbWarmupExercise = filterExercises(genData,
                                           ["muscle_group", "main_lift"],
                                           [["Full"], ["No"]]
                                           ).exercise.sample(1).tolist()

        warmupExercises = fbWarmupExercise
        warmupExercises.extend(warmupData.exercise.sample(2).tolist())

        warmup = {}

        for i in range(3):
            warmup[warmupExercises[i][0]] = warmupRR

        self.setWarmup(warmup)

    def generateRoutine(self):
        """
        Uses class properties to output a workout warmup. Returns a dict,
        of key:value pairs where key is an exercise with a value of an
        of one set's worth of work
        """

        genData = self.getData()
        target = self.getTarget()
        allParts = self.getParts()
        repRanges = self.getRepRanges()
        gear = self.getGear()

        routine = {}

        if allParts is None:

            # Mixed cardio workout
            if target == "both":
                routine = makeMixedRoutine(genData, repRanges)

            elif target == "regular":
                routine = makeRegularRoutine(genData, repRanges, gear)

            elif target == "hiit":
                routine = makeHiitRoutine(genData, repRanges)

            self.setRoutine(routine)

        # Calisthenics workout i.e. no gym
        elif gear == "gymless":
            routine = makeCalisthenicsRoutine(genData, target, repRanges)
            self.setRoutine(routine)

        # Else weight training (Each part in part should be the major focus
        # of at least one exercise and the minor focus in at least one more.)
        else:
            # If full body, get 6 exercises and assign reps
            if target == "full":
                routine = makeFullBodyRoutine(genData, repRanges)
                self.setRoutine(routine)
            else:
                # Make routine
                routine = makeWeightRoutine(genData, target, repRanges,
                                            allParts)
                self.setRoutine(routine)

    # Format warmup & routine as dataframe and assign appropriate sets
    def formatFullRoutine(self):
        """
        Requires routine & warmup to be generated. Returns 2 dataframes,
        in a list, one created from the warmup and one from the routine, both
        will contain all exercises, the contents of a set & the number of sets
        per exercise.
        """
        # Get routine and warmup
        routine = self.getRoutine()
        warmup = self.getWarmup()

        # Ensure routine &/| warmup exists
        if {} in [routine, warmup]:

            raise ValueError("""
                             Routine & warmup must not be empty: generate
                             using generateWarmup() or generateRoutine()."""
                             )

        # Convert dicts into DataFrames
        warmupDF = pd.DataFrame.from_dict(warmup, orient="index")
        routineDF = pd.DataFrame.from_dict(routine, orient="index")

        # Add rest row
        rests = pd.DataFrame.from_dict({
            "Rest": ["15 seconds", "30 seconds", "45 seconds"]
            }, orient="index")

        # Also add index col as exercise list
        warmupDF = warmupDF.append(rests).reset_index(drop=False)

        # Change column names of warmup
        warmupDF = warmupDF.rename(index=str, columns={
            0: "Circuit 1",
            1: "Circuit 2",
            2: "Circuit 3",
            "index": "Exercise"
            })

        # Make set -> reps map dict
        setMap = {
            # Weight options
            "5": 5,
            "3-5": 5,
            "8-12": 3,
            "10-15": 4,
            "12-15": 4,

            # Cardio options
            "8 mins": 1,
            "15 seconds":  4,
            "10 seconds": 3,
            "5 mins": 2,
            "30 seconds": 2
            }

        # Get set counts
        setCount = routineDF.iloc[:, 0].apply(lambda reps: setMap[reps])

        # Add set numbers to routine
        routineDF.insert(0, "Sets", setCount, allow_duplicates=True)

        # Add exercises as column from index
        routineDF = routineDF.reset_index(drop=False)

        # Fix column names
        routineDF = routineDF.rename(index=str, columns={
            "index": "Exercise",
            0: "Reps"})

        # return lists of 2 DFs
        return [warmupDF, routineDF]


def returnWorkout(data, goal, groupOrCardio, gear):
    """
    Returns a workout class object from inputed args from user
    """
    # Go through every column and filter out all the data we need per the
    # user inputs

    # Initialise reference dicts for body parts and for goals
    bodyDict = {
        "chest": ["Pec Major", "Pec Minor"],
        "shoulders": ["Rear Delt", "Mid Delt", "Front Delt"],
        "back": ["Upper Back", "Mid Back", "Lower Back", "Lats", "Traps"],
        "legs": ["Quads", "Hamstrings", "Calves"],
        "arms": ["Biceps", "Triceps"],
        "core": ["Core", "Obliques"],
        "full": ["Full Body"]
    }

    allRanges = {
        "low": ["3-5"],
        "mix": ["5", "8-12", "10-15"],
        "high": ["12-15"],

        "cardio": {
            "regular": ["8 mins"],
            "hiit": ["15 seconds"],
            "both": {
                "Plyo": "10 seconds",
                "Cardio": "5 mins"
            }
        }
    }

    # Initially filter down by gear

    if gear == "gymless":
        data = filterExercises(data, ["gym_level"], [["Gymless"]])

    elif gear == "basic":
        data = filterExercises(data, ["gym_level"],
                               [["None", "Gymless", "Basic"]])

    # Get repRanges for the specified goal
    repRanges = allRanges[goal]

    # Cardio process is different so check the goal input
    if goal == "cardio":

        # Check the cardio value for rep range
        repRanges = repRanges[groupOrCardio]

        # Assign body parts variable (For object) to None
        allParts = None

        # Filter for cardio exercises only

        data = filterExercises(data, ["exercise_type"], [["Cardio", "Plyo"]])

    else:

        # Get full body exercise for warmup
        fullBody = filterExercises(data, ["muscle_group"],
                                   [["Full"]])
        # Filter data for body part
        data = filterExercises(data, ["muscle_group"],
                               [[groupOrCardio.capitalize()]])

        # Drop deadlift
        fullBody.drop(fullBody[fullBody.main_lift == "Yes"].index)

        # Append together
        data = data.append(fullBody, ignore_index=True)

        # All parts assigned from bodyDict
        allParts = bodyDict[groupOrCardio]

    # Finalise Workout object args
    target = groupOrCardio

    workoutObj = Workout(data, target, allParts, repRanges, gear)

    return workoutObj
