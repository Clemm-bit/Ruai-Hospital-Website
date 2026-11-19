from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .payment_models import Payment
from .payment_serializers import PaymentSerializer


class PaymentListView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        queryset = Payment.objects.select_related(
            "patient__user",
            "appointment"
        )

        if user.role in ["super_admin", "receptionist"]:
            return queryset.order_by("-payment_date")

        if user.role == "patient":
            return queryset.filter(
                patient__user=user
            ).order_by("-payment_date")

        return queryset.none()


class PaymentDetailView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "payment_id"

    def get_queryset(self):
        user = self.request.user

        queryset = Payment.objects.select_related(
            "patient__user",
            "appointment"
        )

        if user.role in ["super_admin", "receptionist"]:
            return queryset

        if user.role == "patient":
            return queryset.filter(patient__user=user)

        return queryset.none()
