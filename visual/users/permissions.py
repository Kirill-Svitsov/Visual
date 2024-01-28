from rest_framework import permissions

class IsUserOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST':
            # Разрешить POST-запрос для создания пользователя
            return True

        user_id = request.data.get('id')
        try:
            return request.user.is_staff or request.user.id == int(user_id)
        except (ValueError, TypeError):
            return False
