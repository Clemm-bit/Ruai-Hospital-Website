from django.db import models
from .patient_models import Patient
from .doctor_models import Doctor


class Appointment(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
        ("in_progress", "In Progress"),
        ("no_show", "No Show"),
    ]

    appointment_id = models.AutoField(primary_key=True)

    patient = models.ForeignKey(
        Patient,
        db_column="patient_id",
        on_delete=models.DO_NOTHING,
        related_name="appointments"
    )

    doctor = models.ForeignKey(
        Doctor,
        db_column="doctor_id",
        on_delete=models.DO_NOTHING,
        related_name="appointments"
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    reason = models.TextField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "appointments"
        managed = False

    def __str__(self):
        return f"Appointment {self.appointment_id}"
