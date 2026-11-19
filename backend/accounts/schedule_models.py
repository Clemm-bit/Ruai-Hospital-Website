from django.db import models
from .doctor_models import Doctor


class DoctorSchedule(models.Model):

    DAYS_OF_WEEK = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]

    schedule_id = models.AutoField(primary_key=True)

    doctor = models.ForeignKey(
        Doctor,
        db_column="doctor_id",
        on_delete=models.DO_NOTHING,
        related_name="schedules"
    )

    day_of_week = models.PositiveSmallIntegerField(
        choices=DAYS_OF_WEEK
    )

    start_time = models.TimeField()
    end_time = models.TimeField()
    slot_duration = models.PositiveIntegerField(default=30)

    effective_from = models.DateField(null=True, blank=True)
    effective_until = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "doctor_schedules"
        managed = False

    def __str__(self):
        return f"{self.doctor.user.full_name} - {self.get_day_of_week_display()}"
