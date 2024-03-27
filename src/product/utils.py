from rest_framework import permissions


class IsOwnerReview(permissions.BasePermission):
    """
    Custom permission to tell who is owner of review
    """
    def has_object_permission(self, request, view, obj):
        return (
                str(obj.author.username) == request.user.username or
                bool(request.user and request.user.is_superuser)
        )
