from rest_framework import viewsets, permissions, filters
from django.db.models import Prefetch

from CMS_Backend.core.permission import PublicListPermissionMixin

from team_api.models import TeamMember, TeamMemberSocial

from team_api.serializers import TeamMemberSerializer


class TeamMemberViewSet(PublicListPermissionMixin, viewsets.ModelViewSet):
    """
        Team Member CRUD + Public Read API
    """
    serializer_class = TeamMemberSerializer
    lookup_field = "slug"

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "name",
        "designation",
        "short_bio",
    ]

    ordering_fields = [
        "order",
        "created_at",
        "name",
    ]

    ordering = ["order"]

    def get_permissions(self):
        """
        - Read: Public
        - Write: Admin only
        """
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_queryset(self):
        """
        Queryset rules:
        - Public: only active + visible
        - Admin: all
        """
        qs = TeamMember.objects.prefetch_related(
            Prefetch(
                "social_profiles",
                queryset=TeamMemberSocial.objects.select_related(
                    "platform").order_by("order")
            )
        )

        if self.request.user.is_staff:
            return qs

        return qs.filter(
            is_active=True,
            status=True,
        )

    def perform_destroy(self, instance):
        """
        Soft delete instead of hard delete
        """
        instance.soft_delete()
