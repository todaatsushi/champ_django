from django.contrib import admin
from django.urls import path

import workouts.views as v


urlpatterns = [
    path('config/', v.config, name='champ-config')
]
