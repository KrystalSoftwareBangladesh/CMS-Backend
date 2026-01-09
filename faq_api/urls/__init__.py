from django.urls import path, include

from .faq import urlpatterns as faq_urlpatterns


urlpatterns = [
    path('', include(faq_urlpatterns)),
]
