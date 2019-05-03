from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

import workouts.api.views as av


urlpatterns = [
     # Root
     path('', av.champ_api_root, name='champ-api-root'),

     # Exercises
     path('exercises/', av.ExerciseList.as_view(),
          name='exercise-list'),
     path('exercises/<int:pk>/', av.ExerciseDetail.as_view(),
          name='exercise-detail'),

     # Users
     path('users/', av.UserList.as_view(),
          name='user-list'),
     path('users/<int:pk>/', av.UserDetail.as_view(),
          name='user-detail'),

     # Login
     path('auth/', include('rest_framework.urls'),
          name='api-auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
