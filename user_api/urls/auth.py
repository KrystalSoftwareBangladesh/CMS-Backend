from django.urls import path

from user_api import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
]
