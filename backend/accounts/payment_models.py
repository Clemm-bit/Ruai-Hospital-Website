from django.db import models
from .patient_models import Patient
from .appointment_models import Appointment


class Payment(models.Model):

    PAYMENT_METHOD_CHOICES = [
        ("cash", "Cash"),
        ("mpesa", "M-Pesa"),
        ("card", "Card"),
        ("bank_transfer", "Bank Transfer"),
        ("insurance", "Insurance"),
    ]

    PAYMENT_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    ]

    payment_id = models.AutoField(primary_key=True)

    patient = models.ForeignKey(
        Patient,
        db_column="patient_id",
        on_delete=models.DO_NOTHING,
        related_name="payments"
    )

    appointment = models.ForeignKey(
        Appointment,
        db_column="appointment_id",
        on_delete=models.DO_NOTHING,
        related_name="payments",
        null=True,
        blank=True
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="pending",
        null=True,
        blank=True
    )

    transaction_reference = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        blank=True
    )

    payment_date = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = "payments"
        managed = False

    def __str__(self):
        return f"Payment {self.payment_id}"
