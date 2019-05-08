from rest_framework.permissions import IsAdminUser, SAFE_METHODS


class IsAdminOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        print(request.method in SAFE_METHODS, is_admin)
        return request.method in SAFE_METHODS or is_admin
