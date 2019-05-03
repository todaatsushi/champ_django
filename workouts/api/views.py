from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from workouts.models import Exercise
from workouts.api.serializers import ExerciseSerializer, UserSerializer
from workouts.api.permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def champ_api_root(request, format=None):
    return Response({
        'users': reverse('champ-api-user_list', request=request,
                         format=format),
        'exercises': reverse('champ-api-exercise_list',
                             request=request, format=format),
    })


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    List, create, retrieve, update & destroy actions on the Exercise model.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List & detail on the User model.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
