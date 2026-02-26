from rest_framework import serializers
from ..models import CustomUser


# Admin uchun user list serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "role", "is_active", "is_staff", "created_at"]


# Admin uchun user detail serializer
class AdminUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "role",
            "is_active",
            "is_staff",
            "is_superuser",
            "created_at",
        ]
