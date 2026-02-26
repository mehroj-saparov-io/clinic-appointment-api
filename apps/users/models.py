from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class CustomUserManager(BaseUserManager):
    # Bu yerda oddiy user yaratayabman
    # Bunda ularga role berishim mumkin, defaultda esa "patient" roli beriladi
    # Qachon doctor yaratmoqchi bo'lsam, role ni "doctor" qilib beramiz
    def create_user(self, username, password=None, role="patient", **extra_fields):
        if not username:
            raise ValueError("Username kerak")
        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Bu yerda superuser yaratayabman, unga admin roli beriladi va is_staff, is_superuser ham True qilinadi
    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(username, password, role="admin", **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("doctor", "Doctor"),
        ("patient", "Patient"),
    )

    username = models.CharField(max_length=150, unique=True)
    # Bu yerda role ni tanlashim mumkin, defaultda esa "patient" roli beriladi
    # max_length ni 10 qilib qo'ydim, lekin 7 qilsak ham bo'ladi
    # chunki "patient" so'zi 7 ta harfdan iborat, "doctor" ham 6 ta harfdan iborat, "admin" esa 5 ta harfdan iborat
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Bu yerda is_staff ni defaultda False qilib qo'ydim, chunki faqat adminlar is_staff bo'lishi kerak
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []  # USERNAME_FIELD dan tashqari, superuser yaratishda kerak bo'ladigan maydonlar
    # masalan, email kerak bo'lsa, bu yerga "email" ni qo'shishim mumkin

    def __str__(self):
        return f"{self.username} - ({self.role})"


class DoctorProfile(models.Model):
    GENDER_CHOICES = (("male", "Male"), ("female", "Female"))

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="doctor_profile"
    )
    specialization = models.CharField(max_length=255)
    experience_years = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.specialization})"


class PatientProfile(models.Model):
    GENDER_CHOICES = (("male", "Male"), ("female", "Female"))

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="patient_profile"
    )
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.user.username}"
