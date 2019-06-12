from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('home.urls')),
    path('workouts/', include('workouts.urls')),
    path('api/', include('workouts.api.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
