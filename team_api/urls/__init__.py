from django.urls import path, include

from .team import urlpatterns as team_urlpatterns


urlpatterns = [
    path('', include(team_urlpatterns)),
]
