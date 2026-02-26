import django_filters
from .models import Appointment


class AppointmentFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name="timeslot__date")
    status = django_filters.CharFilter(field_name="status")
    doctor = django_filters.NumberFilter(field_name="doctor__id")

    class Meta:
        model = Appointment
        fields = ["date", "status", "doctor"]
