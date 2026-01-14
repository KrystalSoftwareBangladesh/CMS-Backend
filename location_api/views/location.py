from rest_framework import viewsets, permissions, filters

from location_api.models import OfficeLocation

from location_api.serializers import (
    OfficeLocationSerializer,
    # OfficeLocationListSerializer,
)


class OfficeLocationViewSet(viewsets.ModelViewSet):
    lookup_field = "slug"
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "name",
        "country",
        "city",
        "address",
    ]

    ordering_fields = [
        "order",
        "country",
        "city",
    ]

    ordering = ["order"]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_serializer_class(self):
        # if self.action == "list":
        #     return OfficeLocationListSerializer
        return OfficeLocationSerializer

    def get_queryset(self):
        qs = OfficeLocation.objects.all()

        # Public visibility rules
        if not self.request.user.is_staff:
            qs = qs.filter(
                is_active=True,
                status=True,
            )

        # Optional filters
        country = self.request.query_params.get("country")
        if country:
            qs = qs.filter(country__iexact=country)

        is_featured = self.request.query_params.get("is_featured")
        if is_featured in ["true", "false"]:
            qs = qs.filter(is_featured=is_featured == "true")

        return qs

    def perform_destroy(self, instance):
        instance.soft_delete()
