from rest_framework.routers import DefaultRouter
from news_api import views

router = DefaultRouter()
router.register("", views.NewsViewSet, basename="news")

urlpatterns = router.urls
