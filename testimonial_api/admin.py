# testimonials/admin.py
from django.contrib import admin
from django.utils.html import format_html

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "designation",
        "company",
        "rating_display",
        "is_featured",
        "order",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_featured",
        "rating",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "company",
        "designation",
        "message",
    )

    ordering = ("order", "-created_at")

    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )

    fieldsets = (
        ("Person Details", {
            "fields": (
                "name",
                "designation",
                "company",
            )
        }),
        ("Testimonial Content", {
            "fields": (
                "message",
            )
        }),
        ("Media & Rating", {
            "fields": (
                "avatar",
                "rating",
            )
        }),
        ("Display Settings", {
            "fields": (
                "is_featured",
                "order",
            )
        }),
        ("System", {
            "fields": (
                "is_active",
                "deleted_at",
                "created_at",
                "updated_at",
            )
        }),
    )

    actions = [
        "mark_active",
        "mark_inactive",
        "mark_featured",
        "unmark_featured",
    ]

    @admin.action(description="Mark selected testimonials as active")
    def mark_active(self, request, queryset):
        queryset.update(is_active=True, deleted_at=None)

    @admin.action(description="Soft delete selected testimonials")
    def mark_inactive(self, request, queryset):
        for obj in queryset:
            obj.soft_delete()

    @admin.action(description="Mark selected testimonials as featured")
    def mark_featured(self, request, queryset):
        queryset.update(is_featured=True)

    @admin.action(description="Unmark selected testimonials as featured")
    def unmark_featured(self, request, queryset):
        queryset.update(is_featured=False)

    def rating_display(self, obj):
        """
        Nicely display rating in admin list.
        """
        if obj.rating:
            return format_html(
                "<span title='{} / 5'>⭐ {}</span>",
                obj.rating,
                obj.rating
            )
        return "-"

    rating_display.short_description = "Rating"
