from rest_framework import serializers
from .payment_models import Payment


class PaymentSubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            "appointment",
            "amount",
            "payment_method",
            "transaction_reference",
        ]

    def validate_payment_method(self, value):
        if value != "mpesa":
            raise serializers.ValidationError(
                "Only M-Pesa submissions are accepted through this endpoint."
            )
        return value

    def validate_transaction_reference(self, value):
        if not value:
            raise serializers.ValidationError(
                "Please provide your M-Pesa transaction code."
            )

        value = value.strip().upper()

        if Payment.objects.filter(transaction_reference__iexact=value).exists():
            raise serializers.ValidationError(
                "This M-Pesa transaction code has already been submitted."
            )

        return value
