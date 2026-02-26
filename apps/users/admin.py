from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, DoctorProfile, PatientProfile


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("id", "username", "role", "is_active", "is_staff", "is_superuser")
    list_filter = ("role", "is_active", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("username", "password", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "role",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    search_fields = ("username",)
    ordering = ("id",)


class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "specialization", "experience_years", "gender")
    search_fields = ("user__username", "specialization")


class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "phone", "date_of_birth", "gender")
    search_fields = ("user__username", "phone")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(DoctorProfile, DoctorProfileAdmin)
admin.site.register(PatientProfile, PatientProfileAdmin)
