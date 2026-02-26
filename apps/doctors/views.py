from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.users.models import DoctorProfile
from apps.timeslots.models import TimeSlot
from apps.timeslots.serializers import TimeSlotSerializer
from .serializers import DoctorSerializer
from .filters import DoctorFilter


class DoctorListView(generics.ListAPIView):
    queryset = DoctorProfile.objects.select_related("user")
    serializer_class = DoctorSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_class = DoctorFilter
    search_fields = ["specialization", "user__username"]


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = DoctorProfile.objects.select_related("user")
    serializer_class = DoctorSerializer


class DoctorTimeSlotListView(generics.ListAPIView):
    serializer_class = TimeSlotSerializer

    def get_queryset(self):
        doctor_id = self.kwargs["pk"]
        return TimeSlot.objects.filter(
            doctor_id=doctor_id, is_available=True
        ).select_related("doctor")
