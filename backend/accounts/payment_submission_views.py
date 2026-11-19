from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

from .patient_models import Patient
from .payment_models import Payment
from .payment_submission_serializers import PaymentSubmissionSerializer


class PaymentSubmissionView(generics.CreateAPIView):

    serializer_class = PaymentSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        if user.role != "patient":
            raise PermissionDenied(
                "Only patients can submit payments."
            )

        patient = Patient.objects.filter(user=user).first()

        if not patient:
            raise PermissionDenied(
                "Patient profile not found."
            )

        serializer.save(
            patient=patient,
            payment_status="pending"
        )
