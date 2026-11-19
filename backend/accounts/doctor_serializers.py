from rest_framework import serializers
from .doctor_models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.full_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    phone = serializers.CharField(source="user.phone", read_only=True)
    department_name = serializers.CharField(
        source="department.department_name",
        read_only=True
    )

    class Meta:
        model = Doctor
        fields = [
            "doctor_id",
            "user",
            "full_name",
            "email",
            "phone",
            "department",
            "department_name",
            "specialization",
            "qualification",
            "license_number",
            "bio",
            "consultation_fee",
            "availability_status",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "doctor_id",
            "created_at",
            "updated_at",
        ]
