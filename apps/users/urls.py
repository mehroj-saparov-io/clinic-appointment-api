from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    LoginView,
    MeView,
    DoctorProfileView,
    PatientProfileView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", MeView.as_view(), name="me"),
    path("doctor/profile/", DoctorProfileView.as_view(), name="doctor-profile"),
    path("patient/profile/", PatientProfileView.as_view(), name="patient-profile"),
    path("", include("apps.users.admin_urls")),
]
