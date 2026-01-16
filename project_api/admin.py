from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # List page
    list_display = (
        "title",
        "service",
        "is_featured",
        "status",
        "order",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "service",
        "is_featured",
        "status",
        "created_at",
    )
    search_fields = (
        "title",
        "short_description",
        "description",
    )
    ordering = ("order", "-created_at")

    # Detail page
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at", "deleted_at")

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "service",
                    "short_description",
                    "description",
                    "cover_image",
                )
            },
        ),
        (
            "UI Metrics",
            {
                "fields": (
                    "deliveries_count",
                    "countries_count",
                    "on_time_rate",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Visibility & Highlight",
            {
                "fields": (
                    "is_featured",
                    "status",
                    "order",
                )
            },
        ),
        (
            "System Fields",
            {
                "fields": (
                    "is_active",
                    "created_at",
                    "updated_at",
                    "deleted_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )

    # Performance & UX
    list_select_related = ("service",)
    list_editable = ("order", "is_featured", "status")
    save_on_top = True

    # Soft delete safety
    actions = ["soft_delete_selected", "restore_selected"]

    def soft_delete_selected(self, request, queryset):
        queryset.update(is_active=False)
    soft_delete_selected.short_description = "Soft delete selected projects"

    def restore_selected(self, request, queryset):
        queryset.update(is_active=True, deleted_at=None)
    restore_selected.short_description = "Restore selected projects"
