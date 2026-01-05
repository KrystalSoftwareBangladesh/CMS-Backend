from django.urls import path, include

from .auth import urlpatterns as auth_urlpatterns
from .user import urlpatterns as user_urlpatterns

urlpatterns = [
    path('auth/', include((auth_urlpatterns, 'auth'))),
    path('user/', include((user_urlpatterns, 'user'))),
]
