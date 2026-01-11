from django.urls import path, include

from .social import urlpatterns as social_urlpatterns


urlpatterns = [
    path('', include(social_urlpatterns)),
]
