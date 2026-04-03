from rest_framework.permissions import BasePermission

class BaseRolePermission(BasePermission):
    allowed_roles = []

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role in self.allowed_roles
        )


class IsAdmin(BaseRolePermission):
    allowed_roles = ['admin']


class IsAnalyst(BaseRolePermission):
    allowed_roles = ['admin', 'analyst']


class IsViewer(BaseRolePermission):
    allowed_roles = ['admin', 'analyst', 'viewer']