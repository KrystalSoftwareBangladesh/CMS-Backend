# from django.urls import path
from rest_framework.routers import DefaultRouter

from project_api import views


router = DefaultRouter()


router.register(r'', views.ProjectViewSet, basename='projects')


urlpatterns = []

urlpatterns += router.urls
