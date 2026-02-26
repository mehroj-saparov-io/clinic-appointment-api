import django_filters
from apps.users.models import DoctorProfile


class DoctorFilter(django_filters.FilterSet):
    specialization = django_filters.CharFilter(
        field_name="specialization", lookup_expr="icontains"
    )

    experience_years = django_filters.NumberFilter(
        field_name="experience_years", lookup_expr="gte"
    )

    class Meta:
        model = DoctorProfile
        fields = [
            "specialization",
            "experience_years",
        ]
