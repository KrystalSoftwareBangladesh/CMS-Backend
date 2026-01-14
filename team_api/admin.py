# team_api/admin.py
from django.contrib import admin

from .models import TeamMember, TeamMemberSocial


class TeamMemberSocialInline(admin.TabularInline):
    model = TeamMemberSocial
    extra = 1
    ordering = ("order",)
    autocomplete_fields = ("platform",)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "designation",
        "is_featured",
        "status",
        "order",
        "created_at",
    )
    list_filter = (
        "designation",
        "is_featured",
        "status",
    )
    search_fields = (
        "name",
        "designation",
        "short_bio",
    )
    ordering = ("order", "-created_at")

    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at", "deleted_at")

    inlines = (TeamMemberSocialInline,)

    list_editable = ("order", "is_featured", "status")
    save_on_top = True

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "slug",
                    "designation",
                    "profile_image",
                    "short_bio",
                    "bio",
                )
            },
        ),
        (
            "Visibility",
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
