from rest_framework.permissions import IsAdminUser, SAFE_METHODS


class IsAdminOrReadOnly(IsAdminUser):
    """
    Only allow editing requests from admin accounts or read only else deny.
    """
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin
