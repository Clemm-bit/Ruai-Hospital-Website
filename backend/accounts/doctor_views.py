from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import PermissionDenied, ValidationError

from .doctor_models import Doctor
from .doctor_serializers import DoctorSerializer


class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return Doctor.objects.filter(
            is_active=True
        ).select_related(
            "user", "department"
        ).order_by("user__full_name")

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        if self.request.user.role != "super_admin":
            raise PermissionDenied("Only the superuser can add doctors.")

        doctor_user = serializer.validated_data["user"]

        if doctor_user.role != "doctor":
            raise ValidationError(
                {"user": "The selected user must have the doctor role."}
            )

        serializer.save()


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.select_related(
        "user", "department"
    )
    lookup_field = "doctor_id"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_update(self, serializer):
        if self.request.user.role != "super_admin":
            raise PermissionDenied("Only the superuser can edit doctors.")

        doctor_user = serializer.validated_data.get(
            "user", serializer.instance.user
        )

        if doctor_user.role != "doctor":
            raise ValidationError(
                {"user": "The selected user must have the doctor role."}
            )

        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.role != "super_admin":
            raise PermissionDenied("Only the superuser can delete doctors.")

        instance.delete()
