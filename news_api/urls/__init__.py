from django.urls import path, include

from .news import urlpatterns as news_urlpatterns


urlpatterns = [
    path('', include(news_urlpatterns)),
]
