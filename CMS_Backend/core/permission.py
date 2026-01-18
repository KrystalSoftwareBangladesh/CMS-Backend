# CMS_Backend/core/permission.py
from rest_framework import permissions


class PublicListPermissionMixin:
    def get_permissions(self):
        if self.action == "list":
            return [permissions.AllowAny()]
        return super().get_permissions()
