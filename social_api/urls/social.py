from rest_framework.routers import DefaultRouter

from social_api import views

router = DefaultRouter()


router.register(r"", views.SocialPlatformViewSet, basename="social-platform")

urlpatterns = []
urlpatterns += router.urls
