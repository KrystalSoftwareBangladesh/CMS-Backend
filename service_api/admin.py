# services/admin.py
from django.contrib import admin
# from django.utils.html import format_html

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_featured",
        "order",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_featured",
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    ordering = ("order", "-created_at")

    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )

    fieldsets = (
        ("Basic Info", {
            "fields": (
                "title",
                "slug",
                "description",
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

    actions = ["make_active", "make_inactive"]

    @admin.action(description="Mark selected services as active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True, deleted_at=None)

    @admin.action(description="Mark selected services as inactive (soft delete)")   # noqa
    def make_inactive(self, request, queryset):
        for obj in queryset:
            obj.soft_delete()
