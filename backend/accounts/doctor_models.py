from django.db import models
from accounts.models import User
from accounts.department_models import Department


class Doctor(models.Model):

    AVAILABILITY_CHOICES = [
        ("available", "Available"),
        ("occupied", "Occupied"),
        ("unavailable", "Unavailable"),
    ]

    doctor_id = models.AutoField(primary_key=True)

    user = models.OneToOneField(
        User,
        db_column="user_id",
        on_delete=models.DO_NOTHING,
        related_name="doctor_profile"
    )

    department = models.ForeignKey(
        Department,
        db_column="department_id",
        on_delete=models.DO_NOTHING,
        related_name="doctors"
    )

    specialization = models.CharField(max_length=150)
    qualification = models.CharField(max_length=255, null=True, blank=True)
    license_number = models.CharField(max_length=100, null=True, blank=True, unique=True)
    bio = models.TextField(null=True, blank=True)
    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    availability_status = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default="available"
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "doctors"
        managed = False

    def __str__(self):
        return self.user.full_name
