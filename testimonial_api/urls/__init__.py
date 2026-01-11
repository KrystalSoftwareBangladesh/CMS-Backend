from django.urls import path, include

from .testimonial import urlpatterns as testimonial_urlpatterns


urlpatterns = [
    path('', include(testimonial_urlpatterns)),
]
