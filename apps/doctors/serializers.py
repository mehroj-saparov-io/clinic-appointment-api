from rest_framework import serializers
from apps.users.models import DoctorProfile
from apps.timeslots.models import TimeSlot


class DoctorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = DoctorProfile
        fields = [
            "id",
            "username",
            "specialization",
            "experience_years",
            "gender",
        ]


class DoctorTimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = [
            "id",
            "date",
            "start_time",
            "end_time",
        ]
