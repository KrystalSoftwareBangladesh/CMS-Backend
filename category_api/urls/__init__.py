from django.urls import path, include

from .category import urlpatterns as category_urlpatterns


urlpatterns = [
    path('', include(category_urlpatterns)),
]
