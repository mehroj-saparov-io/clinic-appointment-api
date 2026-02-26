from django.db import models
from django.conf import settings


class TimeSlot(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="timeslots",
        limit_choices_to={"role": "doctor"},
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ["date", "start_time"]
        unique_together = ("doctor", "date", "start_time", "end_time")

    def __str__(self):
        return f"{self.doctor.username} | {self.date} {self.start_time}-{self.end_time}"
