from django.urls import path, include

from .service import urlpatterns as service_urlpatterns


urlpatterns = [
    path('', include(service_urlpatterns)),
]
