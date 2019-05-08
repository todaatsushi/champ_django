from django.urls import path

import home.views as v


urlpatterns = [
    path('', v.home, name='champ-home'),
    path('contact/', v.contact, name='champ-contact'),
    path('about/', v.about, name='champ-about'),
]
