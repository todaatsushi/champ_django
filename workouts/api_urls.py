from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

import workouts.api_views as av


urlpatterns = [
    path('exercises/', av.exercise_list, name='champ-api-exercise_list'),
    path('exercises/<int:pk>/', av.exercise_detail,
         name='champ-api-exercise_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
