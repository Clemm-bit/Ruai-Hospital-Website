from rest_framework import serializers
from .session_models import AppointmentSession


class AppointmentSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppointmentSession
        fields = [
            "session_id",
            "session_name",
            "start_time",
            "end_time",
            "is_active",
            "created_at",
        ]

        read_only_fields = [
            "session_id",
            "created_at",
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
                "end_time": "End time must be later than start time."
            })

        return attrs
