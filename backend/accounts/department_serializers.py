from rest_framework import serializers
from .department_models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            "department_id",
            "department_name",
            "description",
            "location",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["department_id", "created_at"]
