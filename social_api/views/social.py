from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from CMS_Backend.core.permission import PublicListPermissionMixin

from social_api.models import SocialPlatform
from social_api.serializers import SocialPlatformSerializer


class SocialPlatformViewSet(PublicListPermissionMixin, viewsets.ModelViewSet):
    queryset = SocialPlatform.objects.filter(is_active=True)
    serializer_class = SocialPlatformSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "key"]
    ordering_fields = ["created_at", "name"]
    ordering = ["name"]

    def perform_destroy(self, instance):
        instance.soft_delete()
