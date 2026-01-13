from django.urls import path, include

from .project import urlpatterns as project_urlpatterns


urlpatterns = [
    path('', include(project_urlpatterns)),
]
