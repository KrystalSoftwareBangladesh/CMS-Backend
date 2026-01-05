from django.urls import path

from user_api import views

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('list/', views.UserListView.as_view(), name='user-list'),
    path('create/', views.CreateUserView.as_view(), name='user-create'),
]
