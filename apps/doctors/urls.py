from django.urls import path
from .views import DoctorListView, DoctorDetailView, DoctorTimeSlotListView

urlpatterns = [
    path("", DoctorListView.as_view()),
    path("<int:pk>/", DoctorDetailView.as_view()),
    path("<int:pk>/timeslots/", DoctorTimeSlotListView.as_view()),
]
