from django.db import models
from django.utils import timezone


# CHANGE BOOL FIELDS TO CHARFIELDS (KEEP HOW IT WAS BEFORE)
#     OR
# REFACTOR ALL CODES TO REFLECT DJANGO MODEL FIELDS - BOOLEANS/INTS ETC.

class Exercises(models.Model):
    created = models.DateTimeField(default=timezone.now)
    exercise = models.CharField(max_length=100)
    gym_level = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    exercise_type = models.CharField(max_length=100)
    movement_type = models.CharField(max_length=100)
    compound_isolation = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=100)
    major_muscles = models.CharField(max_length=100)
    minor_muscles = models.CharField(max_length=100)
    beginner = models.CharField(max_length=100)
    intermediate = models.CharField(max_length=100)
    advanced = models.CharField(max_length=100)
    sl = models.CharField(max_length=100)
    gvt = models.CharField(max_length=100)
    main_lift = models.CharField(max_length=100)

    owner = models.ForeignKey('auth.User', related_name='exercises',
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.exercise
