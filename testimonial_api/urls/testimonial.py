from rest_framework.routers import DefaultRouter

from testimonial_api import views

router = DefaultRouter()


router.register(r"", views.TestimonialViewSet, basename="testmonial")

urlpatterns = []
urlpatterns += router.urls
