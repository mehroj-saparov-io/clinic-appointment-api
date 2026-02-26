from django.urls import path
from .views import TimeSlotListCreateView, TimeSlotDetailView

urlpatterns = [
    path("", TimeSlotListCreateView.as_view()),
    path("<int:pk>/", TimeSlotDetailView.as_view()),
]
