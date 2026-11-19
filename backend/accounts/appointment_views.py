from django.db import transaction
from django.utils import timezone

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, ValidationError

from .appointment_models import Appointment
from .appointment_serializers import AppointmentSerializer
from .patient_models import Patient
from .doctor_models import Doctor


class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        queryset = Appointment.objects.select_related(
            "patient__user",
            "doctor__user"
        )

        if user.role in ["super_admin", "receptionist"]:
            return queryset.order_by("-start_time")

        if user.role == "patient":
            return queryset.filter(
                patient__user=user
            ).order_by("-start_time")

        if user.role == "doctor":
            return queryset.filter(
                doctor__user=user
            ).order_by("-start_time")

        return queryset.none()

    def perform_create(self, serializer):
        user = self.request.user

        if user.role != "patient":
            raise PermissionDenied(
                "Only registered patients can book appointments."
            )

        start_time = serializer.validated_data["start_time"]
        end_time = serializer.validated_data["end_time"]
        doctor = serializer.validated_data["doctor"]

        if start_time <= timezone.now():
            raise ValidationError({
                "start_time": "Appointment must be booked for a future time."
            })

        if not doctor.is_active:
            raise ValidationError({
                "doctor": "This doctor is not currently available for booking."
            })

        with transaction.atomic():

            # Lock the doctor record while checking for booking conflicts.
            Doctor.objects.select_for_update().get(
                doctor_id=doctor.doctor_id
            )

            overlapping = Appointment.objects.filter(
                doctor=doctor,
                start_time__lt=end_time,
                end_time__gt=start_time,
                status__in=["pending", "confirmed", "in_progress"]
            ).exists()

            if overlapping:
                raise ValidationError({
                    "start_time": "This doctor already has an appointment during that time."
                })

            # Automatically create the patient's profile if it does not exist.
            patient, created = Patient.objects.get_or_create(
                user=user,
                defaults={"created_at": timezone.now()}
            )

            serializer.save(patient=patient)
