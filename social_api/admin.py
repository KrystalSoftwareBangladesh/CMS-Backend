# social/admin.py
from django.contrib import admin
from django.utils.html import format_html

from .models import SocialPlatform


@admin.register(SocialPlatform)
class SocialPlatformAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "key",
        "icon_preview",
        "base_url",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "key",
    )

    ordering = ("name",)

    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )

    fieldsets = (
        ("Platform Info", {
            "fields": (
                "name",
                "key",
                "base_url",
            )
        }),
        ("Icon Settings", {
            "fields": (
                "icon",
                "icon_svg",
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
    ]

    @admin.action(description="Mark selected platforms as active")
    def mark_active(self, request, queryset):
        queryset.update(is_active=True, deleted_at=None)

    @admin.action(description="Soft delete selected platforms")
    def mark_inactive(self, request, queryset):
        for obj in queryset:
            obj.soft_delete()

    def icon_preview(self, obj):
        """
        Shows icon text or SVG indicator in list view.
        """
        if obj.icon_svg:
            return format_html("<span title='SVG icon'>🧩 SVG</span>")
        if obj.icon:
            return format_html("<code>{}</code>", obj.icon)
        return "-"

    icon_preview.short_description = "Icon"
