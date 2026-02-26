from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import RegexValidator
from ..models import CustomUser, DoctorProfile, PatientProfile

phone_validator = RegexValidator(
    regex=r"^\+998\d{9}$",
    message='Phone number must be entered in the format: "+998901234567". 11 digits allowed.',
)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    confirm_password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = CustomUser
        fields = ["username", "password", "confirm_password", "role"]

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.pop("confirm_password")
        if password != confirm_password:
            raise serializers.ValidationError(
                {"password": "Password and Confirm Password do not match."}
            )
        return attrs

    def create(self, validated_data):
        role = validated_data.pop("role", "patient")
        password = validated_data.pop("password")

        user = CustomUser.objects.create_user(
            username=validated_data["username"], password=password, role=role
        )

        # Profillarni yaratish
        if role == "doctor":
            DoctorProfile.objects.create(
                user=user, specialization="", experience_years=0, gender="male"
            )
        elif role == "patient":
            PatientProfile.objects.create(
                user=user, phone="", date_of_birth="2000-01-01", gender="male"
            )

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Username yoki password xato")
            if not user.is_active:
                raise serializers.ValidationError("User aktiv emas")
        else:
            raise serializers.ValidationError("Username va password kerak")

        # JWT token yaratish
        refresh = RefreshToken.for_user(user)
        attrs["user"] = user
        attrs["access"] = str(refresh.access_token)
        attrs["refresh"] = str(refresh)
        return attrs
