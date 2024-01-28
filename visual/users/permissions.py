from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
        Кастомное разрешение, которое позволяет только владельцам объекта редактировать его.
        Позволяет администраторам редактировать любой объект.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST':
            return True
        return request.user and (request.user.is_authenticated or request.user.is_admin)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj and (obj == request.user or request.user.is_admin)
