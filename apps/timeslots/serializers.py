from rest_framework import serializers
from django.utils import timezone
from datetime import datetime
from .models import TimeSlot


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = [
            "id",
            "date",
            "start_time",
            "end_time",
            "is_available",
        ]
        read_only_fields = ["is_available"]

    def validate(self, attrs):
        request = self.context["request"]
        doctor = request.user

        date = attrs.get("date")
        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")

        # start < end
        if start_time >= end_time:
            raise serializers.ValidationError(
                "End time start timedan katta bo‘lishi kerak"
            )

        # past time check — tz-aware qilish
        naive_slot_datetime = datetime.combine(date, start_time)
        slot_datetime = timezone.make_aware(
            naive_slot_datetime, timezone.get_current_timezone()
        )

        if slot_datetime < timezone.now():
            raise serializers.ValidationError(
                "O‘tmishdagi vaqtga TimeSlot yaratib bo‘lmaydi"
            )

        # overlap check
        overlap = TimeSlot.objects.filter(
            doctor=doctor,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time,
        )

        if overlap.exists():
            raise serializers.ValidationError(
                "Bu vaqtda boshqa TimeSlot mavjud (overlap)"
            )

        return attrs

    def create(self, validated_data):
        validated_data["doctor"] = self.context["request"].user
        return super().create(validated_data)
