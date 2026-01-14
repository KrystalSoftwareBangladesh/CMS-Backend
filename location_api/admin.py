from django.contrib import admin

from .models import OfficeLocation


@admin.register(OfficeLocation)
class OfficeLocationAdmin(admin.ModelAdmin):
    # List page
    list_display = (
        "name",
        "country",
        "city",
        "is_head_office",
        "is_featured",
        "status",
        "order",
        "created_at",
    )
    list_filter = (
        "country",
        "is_head_office",
        "is_featured",
        "status",
        "created_at",
    )
    search_fields = (
        "name",
        "country",
        "city",
        "address",
        "phone",
        "email",
    )
    ordering = ("order", "country", "city")

    # Detail page
    prepopulated_fields = {"slug": ("name", "country")}
    readonly_fields = ("created_at", "updated_at", "deleted_at")

    list_editable = (
        "order",
        "is_featured",
        "status",
    )

    save_on_top = True

    fieldsets = (
        (
            "Office Information",
            {
                "fields": (
                    "name",
                    "slug",
                    "country",
                    "city",
                    "address",
                )
            },
        ),
        (
            "Contact Details",
            {
                "fields": (
                    "phone",
                    "email",
                )
            },
        ),
        (
            "Map Coordinates",
            {
                "fields": (
                    "latitude",
                    "longitude",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Visibility & Flags",
            {
                "fields": (
                    "is_head_office",
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

    actions = ["soft_delete_selected", "restore_selected"]

    def soft_delete_selected(self, request, queryset):
        queryset.update(is_active=False)
    soft_delete_selected.short_description = "Soft delete selected offices"

    def restore_selected(self, request, queryset):
        queryset.update(is_active=True, deleted_at=None)
    restore_selected.short_description = "Restore selected offices"
