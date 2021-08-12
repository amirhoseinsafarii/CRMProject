from rest_framework import permissions


class Iscreator(permissions.BasePermission):

    def has_object_permission(self, request, obj):
        if request.user.is_anonymous:
            return False
        if obj.user == request.user:
            return True
        return False