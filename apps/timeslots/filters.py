import django_filters
from .models import TimeSlot


class TimeSlotFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name="date")

    class Meta:
        model = TimeSlot
        fields = ["date"]
