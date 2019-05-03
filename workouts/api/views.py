from djanog.http import Http404

from rest_framework import generics

from workouts.models import Exercise
from workouts.api.serializers import ExerciseSerializer


class ExerciseList(generics.ListCreateAPIView):
    """
    List all exercises / create new exercise entry.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an exercise entry.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
