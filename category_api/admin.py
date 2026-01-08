from django.contrib import admin

from category_api.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # LIST VIEW
    list_display = (
        "name",
        # "content_type",
        # "country_code",
        "parent",
        "is_active",
        "created_at",
    )

    list_filter = (
        # "content_type",
        # "country_code",
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
        "description",
    )

    ordering = (
        # "content_type",
        # "country_code",
        "name",
    )

    # ---------------------------
    # FORM VIEW
    # ---------------------------
    prepopulated_fields = {
        "slug": ("name",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (None, {
            "fields": (
                "name",
                "slug",
                "description",
            )
        }),
        ("Scope", {
            "fields": (
                # "content_type",
                # "country_code",
                "parent",
            )
        }),
        ("Status", {
            "fields": (
                "is_active",
            )
        }),
        ("Audit", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    # ADMIN SAFETY RULES
    # ✅ ONLY enable prepopulation on ADD
    def get_prepopulated_fields(self, request, obj=None):
        if obj:
            return {}
        return {"slug": ("name",)}

    def get_queryset(self, request):
        """
        Exclude soft-deleted categories from admin.
        """
        qs = super().get_queryset(request)
        return qs.filter(deleted_at__isnull=True)

    def save_model(self, request, obj, form, change):
        """
        Auto-assign audit fields.
        """
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user

        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        """
        Make slug read-only after creation (SEO safety).
        """
        if obj:
            return self.readonly_fields + ("slug",)
        return self.readonly_fields
