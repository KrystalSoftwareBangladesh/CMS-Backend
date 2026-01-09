from rest_framework.routers import DefaultRouter
from faq_api import views

router = DefaultRouter()
router.register("", views.FAQViewSet, basename="faq")

urlpatterns = router.urls
