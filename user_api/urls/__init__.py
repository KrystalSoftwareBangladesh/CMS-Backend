from django.urls import path, include

from .auth import urlpatterns as auth_urlpatterns

urlpatterns = [
    path('auth/', include((auth_urlpatterns, 'auth'))),
]
