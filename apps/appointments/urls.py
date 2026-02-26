from django.urls import path
from .views import (
    AppointmentCreateView,
    AppointmentListView,
    AppointmentDetailView,
    AppointmentStatusUpdateView,
)

urlpatterns = [
    path("", AppointmentCreateView.as_view(), name="appointment-create"),
    path("me/", AppointmentListView.as_view(), name="appointment-list"),
    path("<int:pk>/", AppointmentDetailView.as_view(), name="appointment-detail"),
    path(
        "<int:pk>/status/",
        AppointmentStatusUpdateView.as_view(),
        name="appointment-status",
    ),
]
