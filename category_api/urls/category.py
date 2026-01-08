# from django.urls import path
from rest_framework.routers import DefaultRouter

from category_api import views


router = DefaultRouter()


router.register(r'', views.CategoryViewSet, basename='categories')


urlpatterns = []

urlpatterns += router.urls
