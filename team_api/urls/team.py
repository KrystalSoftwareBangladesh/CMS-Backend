from rest_framework.routers import DefaultRouter

from team_api import views

router = DefaultRouter()


router.register(r"", views.TeamMemberViewSet, basename="team")

urlpatterns = []
urlpatterns += router.urls
