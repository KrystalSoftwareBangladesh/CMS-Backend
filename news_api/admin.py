# news_api/admin.py
from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "author_name",
        "read_time_display",
        "is_featured",
        "status",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_featured",
        "status",
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
        "author_name",
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
        ("Content", {
            "fields": (
                "title",
                "slug",
                "category",
                "excerpt",
                "content",
            )
        }),
        ("Media", {
            "fields": (
                "cover_image",
            )
        }),
        ("Meta Information", {
            "fields": (
                "author_name",
                "read_time",
            )
        }),
        ("Display Settings", {
            "fields": (
                "is_featured",
                "status",
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
        "publish",
        "unpublish",
    ]

    # ───────────── Actions ─────────────

    @admin.action(description="Mark selected news as active")
    def mark_active(self, request, queryset):
        queryset.update(is_active=True, deleted_at=None)

    @admin.action(description="Soft delete selected news")
    def mark_inactive(self, request, queryset):
        for obj in queryset:
            obj.soft_delete()

    @admin.action(description="Mark selected news as featured")
    def mark_featured(self, request, queryset):
        queryset.update(is_featured=True)

    @admin.action(description="Unmark selected news as featured")
    def unmark_featured(self, request, queryset):
        queryset.update(is_featured=False)

    @admin.action(description="Publish selected news")
    def publish(self, request, queryset):
        queryset.update(status=True)

    @admin.action(description="Unpublish selected news")
    def unpublish(self, request, queryset):
        queryset.update(status=False)

    # ───────────── Display Helpers ─────────────

    def read_time_display(self, obj):
        return f"{obj.read_time} min"

    read_time_display.short_description = "Read Time"
