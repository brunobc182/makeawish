from rest_framework.compat import is_authenticated
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrSelf(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            request.user and
            is_authenticated(request.user)
        )

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff
