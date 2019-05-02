"""
Tests do not work as expected - solve later.
When run manually in python shell, they work fine.
"""

from django.test import TestCase

from workouts.models import Exercises
from workouts.helpers.Workout import returnWorkout, Workout
import workouts.helpers.helper as h


class HelperTestCase(TestCase):
    # Test helper functions
    def test_check(self):
        true1 = [1 , 2]
        true2 = [3, 1]
        self.assertTrue(h.check(true1, true2))

        false1 = [1, 2]
        false2 = [3, 4]
        self.assertFalse(h.check(false1, false2))

    # Bug in test?
    def test_isinList(self):
        data = h.exerciseData()
        col = 'muscle_group'
        filterAll = [
            ['Chest'],
            ['Chest', 'Arms'],
        ]

        for l in filterAll:
            result = h.isinList(data, col, l)

            # Trues exist
            self.assertTrue(any(result))

            # Falses exists
            self.assertFalse(all(result))

            # Other types bar bools dont exist
            self.assertTrue(
                all(isinstance(x, bool) for x in result)
            )

    def test_filterExercises(self):
        data = h.exerciseData()
        cols = ['exercise_type', 'muscle_group']
        filterList = [['Cardio', 'Plyo'], ['Full', 'Legs']]

        result = h.filterExercises(data, cols, filterList)

        self.assertIsInstance(result, pd.DataFrame)


class WorkoutGeneratorTestCase(TestCase):

    def test_workouts_can_initialise(self):
        data = h.exerciseData()
        goals = [
            ['low', 'mix', 'high'],
            ['cardio']
        ]
        groupOrCardio = [
            ['chest', 'shoulders', 'back', 'arms',
             'legs', 'core', 'full'],
            ['hiit', 'regular', 'both']
        ]
        gear = ['full', 'basic', 'gymless']

        for level in gear:
            for n in [0, 1]:
                for goal in goals[n]:
                    for option in groupOrCardio[n]:
                        print(f'Config: {goal}, {option}, {level}')
                        workout = returnWorkout(data, goal, option, level)
                        print(workout)
                        # self.assertIsInstance(workout, Workout)

                        workout.generateWarmup()
                        print('Warmup finished')
                        workout.generateRoutine()
                        print('Routine finished')

                        result = workout.formatFullRoutine()
                        print('Result formatted')

                        print(workout.getRoutine())
                        print(workout.getWarmup(), '\n')
