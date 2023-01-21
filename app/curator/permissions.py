from rest_framework import permissions


class IsCuratorUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_curator
