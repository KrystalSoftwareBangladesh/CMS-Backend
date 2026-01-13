from rest_framework.routers import DefaultRouter
from service_api import views

router = DefaultRouter()
router.register("", views.ServiceViewSet, basename="service")

urlpatterns = router.urls
