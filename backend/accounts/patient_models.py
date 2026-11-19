from django.db import models
from .models import User


class Patient(models.Model):

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    patient_id = models.AutoField(primary_key=True)

    user = models.OneToOneField(
        User,
        db_column="user_id",
        on_delete=models.DO_NOTHING,
        related_name="patient_profile"
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        null=True,
        blank=True
    )

    address = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    emergency_contact_name = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    emergency_contact_phone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField()

    class Meta:
        db_table = "patients"
        managed = False

    def __str__(self):
        return self.user.full_name
