from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .payment_models import Payment
from .payment_serializers import PaymentSerializer


class PendingPaymentListView(generics.ListAPIView):

    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role not in ["super_admin", "receptionist"]:
            raise PermissionDenied(
                "You are not authorized to view pending payments."
            )

        return Payment.objects.select_related(
            "patient__user",
            "appointment"
        ).filter(
            payment_status="pending"
        ).order_by("-payment_id")
