from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from workouts.api import views as v


# Configure schema
schema_view = get_schema_view(title='Champ API')

# Register viewsets with the Router
router = DefaultRouter()
router.register(r'exercises', v.ExerciseViewSet)
router.register(r'users', v.UserViewSet)


urlpatterns = [
     path('', include(router.urls)),
     path('schema/', schema_view, name='champ-api-schema'),
     path('auth/', include('rest_framework.urls')),
]
