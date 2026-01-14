from rest_framework import serializers

from location_api.models import OfficeLocation


class OfficeLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeLocation
        fields = (
            "id",
            "name",
            "slug",
            "country",
            "city",
            "address",
            "phone",
            "email",
            "latitude",
            "longitude",
            "is_head_office",
            "is_featured",
            "order",
        )
