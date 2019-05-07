from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Exercise(models.Model):

    # Info Fields
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

    # Bool Fields ('Yes', 'No')
    beginner = models.CharField(max_length=10)
    intermediate = models.CharField(max_length=10)
    advanced = models.CharField(max_length=10)
    sl = models.CharField(max_length=10)
    gvt = models.CharField(max_length=10)
    main_lift = models.CharField(max_length=10)

    owner = models.ForeignKey('auth.User', related_name='exercises',
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __repr__(self):
        return self.exercise
