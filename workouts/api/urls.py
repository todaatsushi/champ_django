from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

import workouts.api.views as av


urlpatterns = [
    path('exercises/', av.ExerciseList.as_view(),
         name='champ-api-exercise_list'),
    path('exercises/<int:pk>/', av.ExerciseDetail.as_view(),
         name='champ-api-exercise_detail'),

    path('users/', av.UserList.as_view(),
         name='champ-api-user_list'),
    path('users/<int:pk>/', av.UserDetail.as_view(),
         name='champ-api-user_detail'),

    path('auth/', include('rest_framework.urls'),
         name='champ-api-auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
