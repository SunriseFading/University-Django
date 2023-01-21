from rest_framework import permissions

from curator.models import Curator


class IsCurator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and isinstance(request.user, Curator)
