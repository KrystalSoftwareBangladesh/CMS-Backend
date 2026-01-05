from django.urls import path

from user_api import views

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='profile'),
]
