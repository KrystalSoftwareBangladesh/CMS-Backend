from django.urls import path, include

from .location import urlpatterns as location_urlpatterns


urlpatterns = [
    path('', include(location_urlpatterns)),
]
