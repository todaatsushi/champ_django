"""
User in manage.py shell to import exercises_fin.csv into the database.
"""

import csv
import os

from django.contrib.auth.models import User

from workouts.models import Exercises


me = User.objects.get(id=1)


def makeEntry(row):
    return Exercises(
                exercise=row['Exercise'],
                gym_level=row['GymLevel'],
                equipment=row['Equipment'],
                exercise_type=row['ExerciseType'],
                movement_type=row['MovementType'],
                compound_isolation=row['Compound/Isolation'],
                muscle_group=row['MuscleGroup'],
                major_muscles=row['MajorMuscle'],
                minor_muscles=row['MinorMuscle'],
                beginner='Yes' if row['Beginner'] == 1 else 'No',
                intermediate='Yes' if row['Intermediate'] == 1 else 'No',
                advanced='Yes' if row['Advanced'] == 1 else 'No',
                sl='Yes' if row['SL'] == 1 else 'No',
                gvt='Yes' if row['GVT'] == 1 else 'No',
                main_lift='Yes' if row['MainLift'] == 1 else 'No',
                owner=me,
            )

with open('workouts/helpers/exercises_fin.csv', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        e = makeEntry(row)
        print(True if e else False)
        e.save()
