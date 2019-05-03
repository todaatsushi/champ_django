from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only owners of an exercise can edit/update/delete.
    """
    def has_object_permission(self, request, view, obj):
        # Anyone can read i.e. GET, HEAD, OPTIONS are allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
