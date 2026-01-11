from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter

from testimonial_api.models import Testimonial

from testimonial_api.serializers import TestimonialSerializer


class TestimonialViewSet(ModelViewSet):
    serializer_class = TestimonialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "company", "designation", "message"]
    ordering_fields = ["order", "created_at"]
    ordering = ["order"]

    def get_queryset(self):
        queryset = Testimonial.objects.filter(is_active=True)

        # Optional filter: featured testimonials
        is_featured = self.request.query_params.get("is_featured")
        if is_featured in ["true", "false"]:
            queryset = queryset.filter(is_featured=is_featured == "true")

        return queryset

    def perform_destroy(self, instance):
        instance.soft_delete()
