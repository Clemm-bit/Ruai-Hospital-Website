from rest_framework import serializers
from .schedule_models import DoctorSchedule


class DoctorScheduleSerializer(serializers.ModelSerializer):

    doctor_name = serializers.CharField(
        source="doctor.user.full_name",
        read_only=True
    )

    day_name = serializers.CharField(
        source="get_day_of_week_display",
        read_only=True
    )

    class Meta:
        model = DoctorSchedule
        fields = [
            "schedule_id",
            "doctor",
            "doctor_name",
            "day_of_week",
            "day_name",
            "start_time",
            "end_time",
            "slot_duration",
            "effective_from",
            "effective_until",
            "is_active",
            "created_at",
        ]

        read_only_fields = ["schedule_id", "created_at"]

    def validate(self, attrs):

        start_time = attrs.get(
            "start_time",
            getattr(self.instance, "start_time", None)
        )

        end_time = attrs.get(
            "end_time",
            getattr(self.instance, "end_time", None)
        )

        slot_duration = attrs.get(
            "slot_duration",
            getattr(self.instance, "slot_duration", 30)
        )

        if start_time and end_time and start_time >= end_time:
            raise serializers.ValidationError({
                "end_time": "End time must be later than start time."
            })

        if slot_duration <= 0:
            raise serializers.ValidationError({
                "slot_duration": "Slot duration must be greater than zero."
            })

        return attrs
