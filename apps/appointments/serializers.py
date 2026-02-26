from rest_framework import serializers
from .models import Appointment
from apps.timeslots.models import TimeSlot
from django.utils import timezone
from datetime import datetime


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["id", "doctor", "patient", "timeslot", "status", "created_at"]
        read_only_fields = ["doctor", "patient", "status", "created_at"]

    def validate_timeslot(self, value):
        user = self.context["request"].user

        if user.role != "patient":
            raise serializers.ValidationError(
                "Faqat patient appointment yaratishi mumkin"
            )
        if value.doctor == user:
            raise serializers.ValidationError(
                "Doctor o‘ziga appointment bron qila olmaydi"
            )
        if not value.is_available:
            raise serializers.ValidationError("Bu TimeSlot allaqachon band")

        slot_datetime = timezone.make_aware(
            datetime.combine(value.date, value.start_time)
        )
        if slot_datetime < timezone.now():
            raise serializers.ValidationError(
                "O‘tmishdagi vaqtga appointment bron qilish mumkin emas"
            )
        return value

    def create(self, validated_data):
        user = self.context["request"].user
        timeslot = validated_data["timeslot"]
        appointment = Appointment.objects.create(
            doctor=timeslot.doctor, patient=user, timeslot=timeslot
        )
        timeslot.is_available = False
        timeslot.save()
        return appointment


class AppointmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["status"]
