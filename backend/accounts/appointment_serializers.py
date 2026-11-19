from rest_framework import serializers
from .appointment_models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):

    patient_name = serializers.CharField(
        source="patient.user.full_name",
        read_only=True
    )

    doctor_name = serializers.CharField(
        source="doctor.user.full_name",
        read_only=True
    )

    specialization = serializers.CharField(
        source="doctor.specialization",
        read_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            "appointment_id",
            "patient",
            "patient_name",
            "doctor",
            "doctor_name",
            "specialization",
            "start_time",
            "end_time",
            "reason",
            "status",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "appointment_id",
            "patient",
            "status",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):

        start_time = attrs.get(
            "start_time",
            getattr(self.instance, "start_time", None)
        )

        end_time = attrs.get(
            "end_time",
            getattr(self.instance, "end_time", None)
        )

        if start_time and end_time and start_time >= end_time:
            raise serializers.ValidationError({
                "end_time": "Appointment end time must be later than start time."
            })

        return attrs
