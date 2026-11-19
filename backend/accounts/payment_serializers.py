from rest_framework import serializers
from .payment_models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    patient_name = serializers.CharField(
        source="patient.user.full_name",
        read_only=True
    )

    appointment_id = serializers.IntegerField(
        source="appointment.appointment_id",
        read_only=True
    )

    class Meta:
        model = Payment
        fields = [
            "payment_id",
            "patient",
            "patient_name",
            "appointment_id",
            "amount",
            "payment_method",
            "payment_status",
            "transaction_reference",
            "payment_date",
        ]

        read_only_fields = [
            "payment_id",
            "patient",
            "amount",
            "payment_status",
            "transaction_reference",
            "payment_date",
        ]
