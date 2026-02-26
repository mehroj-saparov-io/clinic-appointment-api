from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import TimeSlot
from .serializers import TimeSlotSerializer
from apps.users.permissions import IsDoctor
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TimeSlotFilter


class TimeSlotListCreateView(generics.ListCreateAPIView):
    serializer_class = TimeSlotSerializer
    permission_classes = [IsAuthenticated, IsDoctor]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TimeSlotFilter

    def get_queryset(self):
        return TimeSlot.objects.filter(doctor=self.request.user)


class TimeSlotDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = TimeSlotSerializer
    permission_classes = [IsAuthenticated, IsDoctor]

    def get_queryset(self):
        return TimeSlot.objects.filter(doctor=self.request.user)

    def perform_destroy(self, instance):
        if not instance.is_available:
            raise PermissionDenied("Band qilingan TimeSlotni o‘chirish mumkin emas")
        instance.delete()
