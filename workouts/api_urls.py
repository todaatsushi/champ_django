from django.urls import path

import workouts.api_views as av


urlpatterns = [
    path('exercises/', av.exercise_list, name='champ-api-exercise_list'),
    path('exercises/<int:pk>/', av.exercise_detail,
         name='champ-api-exercise_detail'),
]