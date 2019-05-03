from django.urls import path, include

from rest_framework.routers import DefaultRouter

from workouts.api import views as v

# Register viewsets with the Router
router = DefaultRouter()
router.register(r'exercises', v.ExerciseViewSet)
router.register(r'users', v.UserViewSet)


urlpatterns = [
     # Root
     path('', include('router.urls'))
]
