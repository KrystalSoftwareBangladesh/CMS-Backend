from rest_framework.routers import DefaultRouter
from location_api import views

router = DefaultRouter()
router.register("", views.OfficeLocationViewSet, basename="office-location")

urlpatterns = router.urls
