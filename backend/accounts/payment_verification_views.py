from django.utils import timezone
from rest_framework import generics, permissions, serializers
from rest_framework.exceptions import PermissionDenied

from .payment_models import Payment


class PaymentVerificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ["payment_id", "payment_status"]
        read_only_fields = ["payment_id"]

    def validate_payment_status(self, value):
        if value not in ["paid", "failed"]:
            raise serializers.ValidationError(
                "Payment status must be paid or failed."
            )

        if self.instance.payment_status != "pending":
            raise serializers.ValidationError(
                "Only pending payments can be verified."
            )

        return value

    def update(self, instance, validated_data):
        instance.payment_status = validated_data["payment_status"]

        if instance.payment_status == "paid":
            instance.payment_date = timezone.now()

        instance.save(update_fields=["payment_status", "payment_date"])
        return instance


class PaymentVerificationView(generics.UpdateAPIView):

    serializer_class = PaymentVerificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Payment.objects.all()
    lookup_field = "payment_id"

    def get_object(self):
        user = self.request.user

        if user.role not in ["super_admin", "receptionist"]:
            raise PermissionDenied(
                "You are not authorized to verify payments."
            )

        return super().get_object()
