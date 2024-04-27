from django.core.exceptions import PermissionDenied
from rest_framework import permissions


class Editor(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied("Доступ запрещён: пользователь не аутентифицирован.")

        if not hasattr(request.user, 'registration'):
            raise PermissionDenied("Доступ запрещён: у пользователя нет профиля.")

        if request.user.registration.role != 'editor':
            raise PermissionDenied("Доступ запрещён: необходимы права редактора.")

        return True
