from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .models import Appointment
from .serializers import AppointmentSerializer, AppointmentStatusSerializer
from .permissions import IsOwnerOrAdmin, IsDoctorOrAdmin, IsPatientOrAdmin
from .filters import AppointmentFilter


# Patient creates appointment
class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsPatientOrAdmin]

    def get_queryset(self):
        return Appointment.objects.all()


class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AppointmentFilter

    def get_queryset(self):
        user = self.request.user
        if user.role == "doctor":
            return Appointment.objects.filter(doctor=user)
        elif user.role == "patient":
            return Appointment.objects.filter(patient=user)
        elif user.role == "admin":
            return Appointment.objects.all()
        return Appointment.objects.none()


class AppointmentDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        return Appointment.objects.all()

    def perform_destroy(self, instance):
        if self.request.user != instance.patient and self.request.user.role != "admin":
            raise PermissionDenied(
                "Faqat patient o‘z appointmentini bekor qilishi mumkin"
            )

        timeslot = instance.timeslot
        timeslot.is_available = True
        timeslot.save()
        instance.delete()


class AppointmentStatusUpdateView(generics.UpdateAPIView):
    serializer_class = AppointmentStatusSerializer
    permission_classes = [IsAuthenticated, IsDoctorOrAdmin]

    def get_queryset(self):
        return Appointment.objects.all()
