from django.contrib import admin

from user_api.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'username', 'email', 'is_deleted']
    list_per_page = 10
    list_display_links = ('full_name', 'username', 'email')
    search_fields = (
        'first_name', 'middle_name', 'last_name', 'username', 'email'
    )
    readonly_fields = ('added_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if "password" in form.changed_data:
            obj.set_password(obj.password)

        super().save_model(request, obj, form, change)
