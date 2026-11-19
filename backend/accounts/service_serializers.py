from rest_framework import serializers
from .service_models import Service


class ServiceSerializer(serializers.ModelSerializer):

    department_name = serializers.CharField(
        source="department.department_name",
        read_only=True
    )

    class Meta:
        model = Service
        fields = [
            "service_id",
            "service_name",
            "description",
            "department",
            "department_name",
            "image_url",
            "is_active",
            "created_at",
        ]

        read_only_fields = [
            "service_id",
            "created_at",
        ]
