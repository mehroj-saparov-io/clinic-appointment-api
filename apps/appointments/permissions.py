from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.patient == request.user
            or obj.doctor == request.user
            or request.user.role == "admin"
        )


class IsDoctorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == "doctor" or request.user.role == "admin"


class IsPatientOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == "patient" or request.user.role == "admin"
