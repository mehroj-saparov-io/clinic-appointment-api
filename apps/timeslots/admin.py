from django.contrib import admin
from .models import TimeSlot


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor", "date", "start_time", "end_time", "is_available")
    search_fields = ("doctor__user__username",)
    list_filter = ("date", "is_available")
    ordering = ("date", "start_time")
