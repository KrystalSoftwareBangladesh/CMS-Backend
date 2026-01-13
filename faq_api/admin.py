# faqs/admin.py
from django.contrib import admin

from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "category",
        "status",
        "order",
        "created_at",
    )

    list_filter = (
        "status",
        "category",
        "created_at",
    )

    search_fields = (
        "question",
        "answer",
    )

    ordering = ("order", "created_at")

    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )

    fieldsets = (
        ("FAQ Content", {
            "fields": (
                "question",
                "answer",
            )
        }),
        ("Classification", {
            "fields": (
                "category",
            )
        }),
        ("Display Settings", {
            "fields": (
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
        "mark_enabled",
        "mark_disabled",
    ]

    @admin.action(description="Mark selected FAQs as active (restore)")
    def mark_active(self, request, queryset):
        queryset.update(is_active=True, deleted_at=None)

    @admin.action(description="Soft delete selected FAQs")
    def mark_inactive(self, request, queryset):
        for obj in queryset:
            obj.soft_delete()

    @admin.action(description="Enable selected FAQs (status = True)")
    def mark_enabled(self, request, queryset):
        queryset.update(status=True)

    @admin.action(description="Disable selected FAQs (status = False)")
    def mark_disabled(self, request, queryset):
        queryset.update(status=False)
