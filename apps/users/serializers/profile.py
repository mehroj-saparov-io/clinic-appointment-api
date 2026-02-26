from rest_framework import serializers
from ..models import CustomUser, DoctorProfile, PatientProfile


# Joriy user ma'lumotlari
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "role"]


# Doctor profile serializer
class DoctorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = DoctorProfile
        fields = ["user", "specialization", "experience_years", "gender"]


# Patient profile serializer
class PatientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PatientProfile
        fields = ["user", "phone", "date_of_birth", "gender"]
